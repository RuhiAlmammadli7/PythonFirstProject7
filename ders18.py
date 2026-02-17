n = 7
if n % 2 == 0:
    print("cut ededdir")
else:
    print("tek ededdir")
# tek ededdir

n = 7
if n % 2:
    print("cut ededdir")
else:
    print("tek ededdir")
# tek ededdir


print(bool(1))
print(bool(0.78))
print(bool(7.8))
# True
print(bool(0))
# False
"""
prioqramlasdirmada:
'1' - True
'0' - False
0-dan basqa hamsi - TRUE
"""


x = 17
print("tek ededdir" if x % 2 else "cut ededdir")
# tek ededdir
result = "tek ededdir" if x % 2 else "cut ededdir"
print(result)
# tek ededdir