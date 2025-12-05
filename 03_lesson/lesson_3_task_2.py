from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16", "+79110001100"),
    Smartphone("Samsung", "A32", "+79001110000"),
    Smartphone("Samsung", "A55", "+79151231232"),
    Smartphone("Xiaomi", "i17 Pro", "+79101100011"),
    Smartphone("Nokia", "3310", "+79143071114")
]

for smartphone in catalog:
    print(smartphone.get_info())
