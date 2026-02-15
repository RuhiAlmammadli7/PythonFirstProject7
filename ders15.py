a = 17
print(10 < a and a < 20)
# True
if (10 < a and a < 20):
    print("10:20")
else:
    print("araliqa daxil deyil")
# 10:20

m = 98
if (10 <= m < 100):
    print("ikireqemli ededdir")
else:
    print("ikireqemli deyil")
# ikireqemli ededdir


b = 11
if (10 < b or b < 20):
    print("10-dan kicik ve ya boyuk")
else:
    print("10-dan boyuk beraber ve 20-den kicik beraber")
# 10-dan kicik ve ya boyuk


print(not 10 < 11)
# print(not True)
# False
print(not 1 > 2)
# print(not False)
# True

c = 200
if (not 9 < c < 100):
    print("ferqli")
else:
    print("ikireqemli ededdir")
# ferqli


# 5 + 2 // 2 * 4
# not > and > or
print(not True and False or False)
# False
print(True or not False and True)
# True


"""
and:
True and False - FALSE
True and True - TRUE
False and False - FALSE

or:
True or False - TRUE
True or True - TRUE
False or False - FALSE

not:
not True - FALSE
not False - TRUE

# Eger bu ucu verilse:
not > and > or
birinci not-a baxilir, sonra and, daha sonra ise or-a baxilir.
"""