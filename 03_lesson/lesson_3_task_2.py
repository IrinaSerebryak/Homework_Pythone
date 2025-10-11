from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "16 pro max", "+79372301626"))
catalog.append(Smartphone("Honor", "50", "+79279576546"))
catalog.append(Smartphone("Xiaomy", "mi1", "+79648927453"))
catalog.append(Smartphone("Huaway", "W61", "+79374659274"))
catalog.append(Smartphone("Samsung", "A56", "+79643674829"))

for phone in catalog:
    print (f"{phone.brand} - {phone.model}. {phone.phone_number}")