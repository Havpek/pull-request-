from Address import Address
from Mailing import Mailing

to_address = Address("294493", "Новосибирск", "Кошурникова", "234", "150")
from_address = Address("88583", "Красноярск", "Булгакова", "23", "15")
mailing = Mailing(to_address, from_address, 600, "SDDS")
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house}, {mailing.from_address.appartment}"
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street},"
      f"{mailing.to_address.house}, {mailing.to_address.appartment}. Стоимость {mailing.cost} рублей")