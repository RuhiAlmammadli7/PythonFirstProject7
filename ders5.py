metn = 'Python'
print(metn)
# Python

metn1 = ("""Python
yaxsidir""")
print(metn1)
# Python
# yaxsidir

#       0123456789
olke = "Azerbaijan"
print(olke[-2])
print(olke[8])
# a

soz = "python"
print(len(soz))
# 6            (length (len) - sozun herf sayini mueyyen edir)

#    0123456789
x = "salam, eli"
print(x[0:5])
print(x[:5])
# salam
print(x[7:10])
print(x[7:])
# eli

#    0123456789
x = "salam, eli"
print(x[:-5])
print(x[0:-5])
# salam
print(x[-3:])
# print(x[-3:]) - sehvdir
# eli


soz = "  jaVa  "
print(soz.upper())
#   JAVA
print(soz.lower())
#   java
print(soz.strip())
# jaVa            (strip - yanlarda olan bosluqlari silir)
print(soz.replace("j","N"))
#   NaVa
print(soz.capitalize())
#   java               (capitalize - ilk indeksi boyuk yazir)
print(soz.count("a"))
# 2                  (count - sirani mueyyen edir)
print(soz.count("ja"))
# 1
print(soz.find("a"))
# 3                 (find - indeksi tapir)
print(soz.find("ja"))
# 2
print(soz.isdigit())
# False             (isdigit - yoxluyurki ededdir yoxsa yox)
print(soz.isalpha())
# False             (isalpha - yoxluyurki elifbadadir yoxsa yox)

a = "Ruhi"
b = "Almamamdli"
print(a+b)
print(a + "" + b)
# RuhiAlmammadli
print(a,b)
print(a + " " + b)
# Ruhi Almammadli     ("" - defoult)

s = "Python"
print(s + s + s)
print(3 * s)
# PythonPythonPython

ad = "Ruhi"
soyad = "Almamamdli"
print("Salam, hormetli {} {}!".format("Ruhi","Almammadli"))
print("Salam, hormetli {} {}!".format(ad,soyad))
print(f"Salam, hormetli {"Ruhi"} {"Almammadli"}!")
print(f"Salam, hormetli {ad} {soyad}!")
# Salam, hormetli Ruhi Almamamdli!

cumle = "Python eyni zaman \"Piton\" kimi adlanir."
cumle = 'Python eyni zaman "Piton" kimi adlanir.'
print(cumle)
# Python eyni zaman "Piton" kimi adlanir.