from smartphone import smartphone
catalog = []
phone1 = smartphone("iPhone", "15 Pro Max", "+79134672828")
phone2 = smartphone("Samsung", "S24 Ultra", "+79234232929")
phone3 =  smartphone("Redmi", "11 Pro+", "+79143222324")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. - {phone.phonenumber}")