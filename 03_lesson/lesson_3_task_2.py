from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15 Pro", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy A31", "+79234567891"))
catalog.append(Smartphone("Poco", "X6 Pro", "+79345678912"))
catalog.append(Smartphone("Nokia", "XR21", "+79456789123"))
catalog.append(Smartphone("Sony", "Xperia 1", "+79567891234"))


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}") # noqa