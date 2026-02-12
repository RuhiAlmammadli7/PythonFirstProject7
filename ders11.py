s = {1,2,3,4,5,6,7,8,9}
print(s)
print(type(s))
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# <class 'set'>
v = {1,2,3,4,5,6,7,8,9,9}
print(v)
# {1, 2, 3, 4, 5, 6, 7, 8, 9} - tekrarlar cap olunmur

ab = {1,2,3,78,90,7,100,-8}
print(ab)
# {1, 2, 3, 100, 7, 78, -8, 90} - sira ile cap olunmur


# print(ab[1]) - ERROR


z = {1,2,3,"True", False}
z.add(7)
print(z)
# {False, 1, 2, 3, 7, 'True'}

b ={"python",3,89,0,False}
b.remove("python")
print(b)
# {89, 3, 0}
# b.remove(1000) - ERROR

f = {1,4,7,"salam"}
f.discard("salam")
print(f)
# {1, 4, 7}
f = {1,4,7,"salam"}
f.discard(1000)
print(f)
# {1, 'salam', 4, 7}

ad = {"ruhi","cavid"}
ad.clear()
print(ad)
# set()
bos_set = set()
print(bos_set)
# set()
asdf = set()
asdf.add("ruhi")
print(asdf)
# {'ruhi'}


x = {2,4,6,8,10,12}
y = {1,3,5,7,9,12}
c = x.union(y)
d = x.intersection(y)
print(c)
print(d)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12} - coxluqlarin birlesmesi
# {12} - coxluqlarin kesismesi

x = {2,4,6,8,10,12}
y = {1,3,5,7,9,12}
c = x.difference(y)
d = y.difference(x)
print(c)
print(d)
# {2, 4, 6, 8, 10}
# {1, 3, 5, 7, 9}


m = {1,2,3,4}
n = m
n.add(5)
print(m,n)
# {1, 2, 3, 4, 5} {1, 2, 3, 4, 5}

m = {1,2,3,4}
n = m.copy()
n.add(5)
print(m,n)
# {1, 2, 3, 4} {1, 2, 3, 4, 5}