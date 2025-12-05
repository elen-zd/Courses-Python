from address import Address
from mailing import Mailing

to_address = Address("123344", "Ивантеевка", "Хлебозаводская", "28", "116")
from_address = Address("143123", "Саратов", "Динамовская", "40б", "27")

mailing = Mailing(to_address, from_address, 2300, "NUM1234567")
print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.home} - {mailing.from_address.appartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.home} "
      f"- {mailing.to_address.appartment}. Стоимость {mailing.cost} рублей.")
