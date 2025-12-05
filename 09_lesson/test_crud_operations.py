import pytest
from sqlalchemy import and_
from models import Student, Course
from datetime import datetime


class TestCRUDOperations:

    def test_create_student(self, db_session):
        """Тест на создание студента - Ирина Серебрякова"""
        new_student = Student(
            name="Ирина Серебрякова",
            email="ira_balakovo_@mail.ru"
        )

        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)

        assert new_student.id is not None
        assert new_student.name == "Ирина Серебрякова"
        assert new_student.email == "ira_balakovo_@mail.ru"
        assert new_student.deleted_at is None


        db_session.delete(new_student)
        db_session.commit()

    def test_update_student(self, db_session):
        """Тест на обновление студента"""

        student = Student(
            name="Ирина Серебрякова",
            email="ira_balakovo_@mail.ru"
        )

        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)

        student_id = student.id


        student.email = "new_ira_balakovo_@mail.ru"
        db_session.commit()


        updated_student = db_session.query(Student).filter(Student.id == student_id).first()
        assert updated_student.email == "new_ira_balakovo_@mail.ru"


        db_session.delete(updated_student)
        db_session.commit()

    def test_soft_delete_course(self, db_session):
        """Тест на мягкое удаление курса"""

        course = Course(
            title="Python программирование",
            description="Курс по основам Python для начинающих от Ирины Серебряковой"
        )

        db_session.add(course)
        db_session.commit()
        db_session.refresh(course)

        course_id = course.id


        available_course = db_session.query(Course).filter(
            and_(Course.id == course_id, Course.deleted_at.is_(None))
        ).first()
        assert available_course is not None


        course.deleted_at = datetime.now()
        db_session.commit()


        deleted_course = db_session.query(Course).filter(
            and_(Course.id == course_id, Course.deleted_at.is_(None))
        ).first()
        assert deleted_course is None


        all_courses = db_session.query(Course).filter(Course.id == course_id).all()
        assert len(all_courses) == 1


        db_session.query(Course).filter(Course.id == course_id).delete()
        db_session.commit()

    def test_create_course(self, db_session):
        """Тест на создание курса"""
        new_course = Course(
            title="Базы данных и SQL",
            description="Изучение Postgres и SQL запросов от Ирины Серебряковой"
        )

        db_session.add(new_course)
        db_session.commit()
        db_session.refresh(new_course)


        assert new_course.id is not None
        assert new_course.title == "Базы данных и SQL"
        assert new_course.deleted_at is None


        db_session.delete(new_course)
        db_session.commit()