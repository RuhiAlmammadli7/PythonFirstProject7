# input - istifadeciden giris melumatlari alinir, yeni istifadeci output yerine yazir
# output - ekrana cap edilen yazi


a = (input())
# output'a yazi yazilmalidir


x = (input("Adinizi qeyd edin: "))
print(x)
print(type(x))
print("Salam, " + x)
print(f"Hormetli musteri, {x}")
# Adinizi qeyd edin: Ruhi
# Ruhi
# <class 'str'>
# Salam, Ruhi
# Hormetli musteri, Ruhi


eded = int(input("Eded daxil edin: "))
print(type(eded))
print(eded ** 2)
# Eded daxil edin: 3
# <class 'int'>
# 9