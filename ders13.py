"""
Ssenari: Havaya gore ne geyinmek lazimdir?

Eger yagis yagirsa:
    - Siz gun eyneyi taxacaqsiniz.

Eger hava guneslidirse:
    - Siz yagmurluq geyineceksiniz.

Eger hava soyuq ve qarlidirsa:
    - Siz isti palto geyineceksiniz.

Basqa cur hava seraiti varsa:
    - Adi geyim geyineceksiniz.
"""

hava = "buludlu"

if hava == "gunesli":
    print("Siz gun eyneyi taxacaqsiniz.")

if hava == "yagisli":
    print("Siz yagmurluq geyineceksiniz.")

if hava == "soyuq ve qarli":
    print("Siz isti palto geyineceksiniz.")

if hava != "gunesli" and hava != "yagisli" and hava != "soyuq ve qarli":
    print("Siz adi geyim geyineceksiniz.")

# Siz adi geyim geyineceksiniz.

print(hava == "gunesli")
# False
print(hava == "buludlu")
# True
print(hava != "yagisli")
# True


# eded 1000-den kicik ve natural ededdir.
eded = 9
if (eded < 10):
    print("Reqemlerin sayi 1")
elif (eded < 100):
    print("Reqemlerin sayi 2")
else:
    print("Reqemlerin sayi 3")

# Reqemlerin sayi 1


"""
'elif' ve 'if' ferqi:
if -- ayri-ayri sert blokudur.
elif -- bir-birine bagli sert blokudur.
Eger bikinci sert bloku True olarsa; (birinci bloka hemse 'if' yazilir)
elif - diger sertlere baxmir
if - diger sertlerede baxir

elif -- else yazmaq mumkundur
if - else yazmaq olur lakin, yazilan sert bloku (else) en son yazilan serte baglidir, qarisiqliq olur. meselen;

hava = "..."

if hava == "gunesli":
    print("Siz gun eyneyi taxacaqsiniz.")

if hava == "yagisli":
    print("Siz yagmurluq geyineceksiniz.")

if hava == "soyuq ve qarli":
    print("Siz isti palto geyineceksiniz.")

else:
    print("Siz adi geyim geyineceksiniz.")

Eger biz 'hava' deyisenine yazsaq bele cap olur:
'yagisli' - Siz yagmurluq geyineceksiniz.
            Siz adi geyim geyineceksiniz.
        "yagisli" → TRUE → ✔ yağmurluq çap olunur
        "soyuq ve qarli" → FALSE → else işə düşür → ✔ adi geyim çap olunur
'soyuq ve qarli' - Siz isti palto geyineceksiniz.
'buludlu' - Siz adi geyim geyineceksiniz.

yeni, axirinci iki sert bloku bir-birine baglidir.
'if' olan hisseler ayri qrupdur.
'else' olan hisse ise ayri qrupdur.
"""