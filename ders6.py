# a = int(1.17) - integer
# a = int("100") - string
# a = int("Python") - ERROR (yalniz reqemden ibaret olmalidir!)
a = 1.17
print(int(a))
print(int(1.17))
# 1
a = int("100")
print(a,type(a))
# 100 <class 'int'>


# b = float(7) - integer
# b = float("2.007") - string
# b = float("python") - ERROR (yalniz reqemden ibaret olmalidir!)
b = 7
print(float(b))
print(float(7))
# 7.0
b = float("2.007")
print(b,type(b))
# 2.007 <class 'float'>


# c = str(12) - string (12 = "12")
# c = str(0.75) - float (0.75 = "0.75")
c = 12
print(str(c))
print(str(12))
# 12
c = str(0.75)
print(c,type(c))
# 0.75 <class 'str'>