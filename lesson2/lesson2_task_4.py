def fizz_buzz(n):
    """
    Функция печатает числа от 1 до n с заменой:
    - Fizz для чисел, делящихся на 3
    - Buzz для чисел, делящихся на 5
    - FizzBuzz для чисел, делящихся на 3 и 5
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizz_buzz(15)