from address import Address
from mailing import Mailing

address_from = Address("682803", "Советская Гавань", "ул. Пионерская", "17", "5") # noqa
address_to = Address("682803", "Советская Гавань", "ул. Спортивная", "1", "43")


my_mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=19.70,
    track="RFRU1234567SVG"
)

# 3. Выводим информацию в требуемом формате
print(f"Отправление {my_mailing.track} из "
      f"{my_mailing.from_address.index}, {my_mailing.from_address.city}, {my_mailing.from_address.street}, {my_mailing.from_address.house} - {my_mailing.from_address.apartment} " # noqa
      f"в "
      f"{my_mailing.to_address.index}, {my_mailing.to_address.city}, {my_mailing.to_address.street}, {my_mailing.to_address.house} - {my_mailing.to_address.apartment}. " # noqa
      f"Стоимость {my_mailing.cost} рублей.") # noqa