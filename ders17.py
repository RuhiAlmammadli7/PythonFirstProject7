list = [1,2,3,4,5]
print(5 in list)
print(7 not in list)
# True
print(5 not in list)
print(7 in list)
# False


tuple = (1,2,3,4,5)
print(5 in tuple)
print(7 not in tuple)
# True
print(5 not in tuple)
print(7 in tuple)
# False


set = {1,2,3,4,5}
print(5 in set)
print(7 not in set)
# True
print(5 not in set)
print(7 in set)
# False


string = "Python"
print("P" in string)
print("H" not in string)
# True
print("tho" not in string)
print("z" in string)
# False


"""
set - isfidesi ucun daha elverislidir (boyuk hcmli melumatlar ucun)
"""


d = {"ad" : "Ruhi"}
print(d["ad"])
print(d["soyad"])
# Ruhi - tekce 'Ruhi'ni cap etdi.
print("ad" in d)
# True
print("soyad" in d)
# False
"""
'in' vasitesile yoxlanilir ve daha sonra xetasiz cap etmek olur.
"""