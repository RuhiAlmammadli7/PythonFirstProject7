programlasdirma_dilleri = ("Python","Java","C++","Javascript","TypeScript")
programlasdirma_dilleri = "Python","Java","C++","Javascript","TypeScript"
print(programlasdirma_dilleri)
# ('Python', 'Java', 'C++', 'Javascript', 'TypeScript')
print(type(programlasdirma_dilleri))
# <class 'tuple'>

z = "Java"
print(type(z))
# <class 'str'>
x = "Java",
# <class 'tuple'>print(type(x))


programlasdirma_dilleri = ("Python","Java","C++")
print(programlasdirma_dilleri[1])
# Java
print(programlasdirma_dilleri[-1])
# C++


ededler = (1,2,3,4,5,6,7)
# ededler[0] = 0 - ERROR
ededler = list(ededler)
print(ededler)
# [1, 2, 3, 4, 5, 6, 7] - artiq list'e cevrildi ve yuxaridaki funksiyani etmek olar
ededler[0] = 0
print(ededler)
# [0, 2, 3, 4, 5, 6, 7] - tipi list'dir
ededler = tuple(ededler)
print(ededler)
# (0, 2, 3, 4, 5, 6, 7)


x = ("Python","Java","C++","Javascript","Javascript")
print(x)
# ('Python', 'Java', 'C++', 'Javascript', 'Javascript')


t = tuple()
t = ()
print(t)
# ()

a = (1,2,3,1)
print(a.count(1))
# 2 - ededden nece dene var
print(a.index(3))
# 2 - yazilan ededin indeksini tapir

ededler1 = (1,2,3,4,5,6)
# ededler1.append(7)
# print(ededler1) - ERROR
ededler1 = list(ededler1)
print(ededler1)
# [1, 2, 3, 4, 5, 6] - artiq list'e cevrildi ve yuxaridaki funksiyani etmek olar
ededler1.append(7)
print(ededler1)
# [1, 2, 3, 4, 5, 6, 7] - tipi list'dir
ededler1 = tuple(ededler1)
print(ededler1)
# (1, 2, 3, 4, 5, 6, 7)