# List'ler ozunde diger tiplerden olan melumatlari saxlaya bilir
# elementler arasinda vergul olmalidir


alinacaqlar_listi = ["Un","Kartof","Pomidor","Corek"]
print(alinacaqlar_listi)
print(type(alinacaqlar_listi))
# ['Un', 'Kartof', 'Pomidor', 'Corek']
# <class 'list'>


liste = ["Xiyar",True,"Pomidor","Xiyar",77,True]
print(liste)
# ['Xiyar', True, 'Pomidor', 'Xiyar', 77, True]


#             0       1      2      3    (alma - 0ci element indeksidir, heyva - 1ci element indeksidir ve s.)
meyveler = ["Alma","Heyva","Nar","Banan"]
print(meyveler[-2])
# Armud
print(meyveler[1:3])
print(meyveler[-3:-1])
# ['Heyva', 'Nar']


terevezler = ["Xiyar","Badimcan","Nar"]
terevezler[-1] = "Qarpiz"
print(terevezler)
# ['Xiyar', 'Badimcan', 'Qarpiz']


#                0         1       2        3
terevezler = ["Xiyar","Badimcan","Nar","Balqabaq"]
terevezler.append("Yemis")
print(terevezler)
# ['Xiyar', 'Badimcan', 'Nar', 'Balqabaq', 'Yemis']

terevezler = ["Xiyar","Badimcan","Nar","Balqabaq"]
terevezler.insert(1,7)
print(terevezler)
# ['Xiyar', 7, 'Badimcan', 'Nar', 'Balqabaq']

terevezler = ["Xiyar","Badimcan","Nar","Balqabaq"]
terevezler.remove("Nar")
print(terevezler)
# ['Xiyar', 'Badimcan', 'Balqabaq']


#                0         1       2        3
terevezler = ["Xiyar","Badimcan","Nar","Balqabaq"]
terevezler.pop()
terevezler.pop(3)
terevezler.pop(-1)
print(terevezler)
# ['Xiyar', 'Badimcan', 'Nar']


x = [7,89,100,-77,0.75]
x.sort()
x.sort(reverse=False)
print(x)
# [-77, 0.75, 7, 89, 100]
x.sort(reverse=True)
print(x)
# [100, 89, 7, 0.75, -77]
x = sorted(x)
x = sorted(x,reverse=False)
print(x)
# [-77, 0.75, 7, 89, 100]
x = sorted(x,reverse=True)
print(x)
# [100, 89, 7, 0.75, -77]

herfler = ["a","c","e","d","f"]
print(sorted(herfler))
# ['a', 'c', 'd', 'e', 'f']
herfler = ["a","c","e","d","f","A","E"]
print(sorted(herfler))
# ['A', 'E', 'a', 'c', 'd', 'e', 'f']


a = [1,2,3,4]
b = a
b.pop()
print(a,b)
# [1, 2, 3] [1, 2, 3]   (list'ler referans tipdir, numunede b a-nin referansini aldi)

a = [1,2,3,4]
b = a.copy()
b.pop()
print(a,b)
# [1, 2, 3, 4] [1, 2, 3]


x = [1,2,3]
y = [3,4,6]
z = x + y
print(z)
# [1, 2, 3, 3, 4, 6]

a = [7] * 3
print(a)
# [7, 7, 7]
b = [7,2] * 3
print(b)
# [7, 2, 7, 2, 7, 2]


ab = [1,2,3,"salam"]
ab.clear()
print(ab)
# []

z = ["salam","alma",7,8,7]
print(z.count("alma"))
# 1
print(z.count(7))
# 2
print(z.count(10))
print(z.count("a"))
# 0

print(z.index(7))
# 2
print(z.index("alma"))
# 1

z.reverse()
z = list(reversed(z))
print(z)
# ['salam', 'alma', 7, 8, 7]

d = list()
d = []
print(d)
# []