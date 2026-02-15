t = (7,8)
print(id(t))
# 2178231168576 - daxil edilen obyektin yaddasdaki yerini temsil eden nomreler


l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1
print(id(l1),id(l2),id(l3),sep=", ")
# 2599633211328, 2599633336000, 2599633211328
l1.append(4)
print(l1,l2,l3)
# [1, 2, 3, 4] [1, 2, 3] [1, 2, 3, 4] - l1 ve l2 referansdir

l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1
print(l1 is l2)
print(l1 is not l3)
# False
print(l1 is l3)
print(l1 is not l2)
# True

a = {2,3,4,5}
b = {2,3,4,5}
print(a == b)
# True
print(a is b)
# False


"""
is - secilen obyektlerin eyni yerde oldugunu yoxlayir
is not - secilern obyektlerin eyni yerde olmadigini yoxlayir

'==' ve 'is' ferqi:
== - iki obyektin deyerlerinin beraberliyini yoxlayir
is - iki obyektin id-nin beraberliyini yoxlayir
"""