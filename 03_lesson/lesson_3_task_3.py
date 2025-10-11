from address import Address
from mailing import Mailing

to_address = Address("102938", "Балаково", "20 лет ВЛКСМ", "16", "26")
from_address = Address("019283", "Самара", "Евгения Золотухина", "26", "16")

mailing = Mailing(to_address=to_address, from_address=from_address, cost=1000, track="TRACK1029384756")

print (f"Отправление{mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")