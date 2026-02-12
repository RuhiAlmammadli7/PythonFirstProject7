#  "acar soz" : "ona qarsiliq gelen deyer"
# insan = {"ad" : "Ruhi"}

insan = {
    "ad" : "Ruhi",
    "soyad" : "Almammadli",
    "tevellud" : "22.03.2007"
}
print(insan)
print(type(insan))
# {'ad': 'Ruhi', 'soyad': 'Almammadli', 'tevellud': '22.03.2007'}
# <class 'dict'>

print(insan.get("ad"))
print(insan["ad"])
# Ruhi

insan = {"ad" : "Ruhi","soyad" : "Almammadli","tevellud" : "22.03.2007","tevellud" : "22.03.2007"}
print(insan)
# {'ad': 'Ruhi', 'soyad': 'Almammadli', 'tevellud': '22.03.2007'}
insan = {"ad" : "Ruhi","soyad" : "Almammadli","tevellud" : "01.03.2010","tevellud" : "22.03.2007"}
print(insan)
# {'ad': 'Ruhi', 'soyad': 'Almammadli', 'tevellud': '22.03.2007'}


car = {"model" : "BMW","year" : "2007",}
print(len(car))
# 2


d = dict()
d = {}
print(d)
# {}


insan1 = {
    "ad" : "Fazil",
    "soyad" : "Feyziyev",
    "tevellud" : "28.01.1999"
}
insan1["ad"] = "Nicat"
print(insan1)
# {'ad': 'Nicat', 'soyad': 'Feyziyev', 'tevellud': '28.01.1999'}

car1 = {"model" : "Audi","year" : "2008",}
car1["qiymet"] = 70000
car1.update({"qiymet": "70000"})
print(car1)
# {'model': 'Audi', 'year': '2008', 'qiymet': 70000}

a = {"ad" : "defter", "vereq sayi" : "100"}
a.pop("vereq sayi")
print(a)
# {'ad': 'defter'}
a.clear()
print(a)
# {}

telefon = {
    "model" : "Iphone",
    "year" : "2020",
    "pil" : "96"
}
print(telefon.keys())
# dict_keys(['model', 'year', 'pil'])
print(telefon.values())
# dict_values(['Iphone', '2020', '96'])
print(telefon.items())
# dict_items([('model', 'Iphone'), ('year', '2020'), ('pil', '96')])