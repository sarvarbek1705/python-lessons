#05-dars matn bilan ishlash --------------------
# ism = "Sarvar"
# familya = "Xalilov"
# print(ism + familya)
# print(ism + ' ' + familya)

#f-string

# ism = "Sarvar"
# familya = "Xalilov"
# ism_sharif = f"{ism} {familya}"
# print(ism_sharif)
# print(f"Mening ismim {ism}, familyam {familya}")

#MAXSUS BELGILAR

# print("hello world")
# print("hello \tworld")
# print("hello \nworld")

# STRING METODLARI

# ism = "sarvar"
# familya = "xalilov"
# ism_sharif = f"{ism} {familya}"
# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize()) # Bunda o'zgaruvchini ichidagi asl qiymat o'zgarmaydi.

# meva = "     olma    "
# print("Men " + meva.lstrip() + " yaxshi ko'raman") # Bunda chap tarafdagi bo'shliqni olib tashlaydi.
# print("Men " + meva.rstrip() + " yaxshi ko'raman") # Bunda o'ng tarafdagi bo'shliqni olib tashlaydi.
# print("Men " + meva.strip() + " yaxshi ko'raman") # Bunda ikki tarafdagi bo'shliqni olib tashlaydi.
# print("Men " + meva + "yaxshi ko'raman")

# INPUT

# ism = input("Ismingiz nima?\n>>>")
# print("Assalomu alaykum " + ism.title())

# 06-dars SONLAR -------------------

# ism = "Sarvar"
# yosh = 25
# xabar = ism + ' ' + str(yosh) + " yoshda" # str() funksiyasi sonni matnga o'tkazadi.
# print(xabar)

# t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh = 2023-t_yil
# print("Sizning yoshingiz " + str(yosh) + " da")

# 07-dars LIST(Ro'yxat) ----------------------

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# narhlar = [12000, 10000, 20000, 30000]
# sonlar = ['bir', 'ikki', 3, 4, 5]
# ismlar = [] # Bo'sh ro'yxat
# print(mevalar[0]) # Ro'yxatdan istalgan qiymatni chiqarib olish uchun uning indeksi bo'yicha chaqiramiz.

# narhlar = [12000, 10000, 30000]
# print(narhlar)
# narhlar[0] = 15000 # Ro'yxat ichidagi biror bir qiymatni o'zgartirish uchun
# print(narhlar[0])

#mevalar = ['olma', 'shaftoli', 'behi']
# print(mevalar)
# mevalar.append('nok') # Bu funksiya ro'yxatni oxiriga yangi qiymat qo'shadi.
# print(mevalar)
# mevalar.insert(0, 'anor') # Bu funksiya ro'yxatga istalgan indeks bo'yicha yangi qiymat qo'shadi.
# print(mevalar)
# mevalar.remove('shaftoli') # Bu funksiya ro'yxatdan istalgan qiymatni o'chiradi.
# print(mevalar)

# del mevalar[0]
# print(mevalar)
# mahsulot = mevalar.pop(1)
# print(mevalar)
# print(mahsulot)

# cars = []
# cars.append('lacetti')
# cars.append('matiz')
# cars.append('damas')
# cars.append('gentra')
# print(cars) # Bo'sh ro'yxatni append() funksiyasi yordamida to'ldirildi.

# bozorlik = ['sabzi', 'piyoz', 'kartoshka', 'banan']
# mahsulot = bozorlik.pop(3)
# print("Olingan mahsulotlar " + mahsulot)
# print("Olinmagan mahsulotlar ", bozorlik)

# 08-dars RO'YXAT BILAN ISHLASH -------------------

# cars = ['bmw', 'general motors', 'tesla', 'mercedes benz', 'audi']
# # cars.sort() # Bu funksiya ro'yxatni alifbo tartibida chiqaradi.
# print(cars)
# cars.sort(reverse=True) # Bu holatda ro'yxat teskari tartibda consolga chiqadi.
# print(cars)
# print(sorted(cars)) # sorted() funksiyasi asl ro'yxatni o'zgartirmasdan tartib bilan chiqaradi.
# print(sorted(cars, reverse=True)) # Ro'yxatni teskari tartibda consolga chiqaradi.
# Bu funksiyalardan sonlardaham foydalanish mumkin.

# cars = ['bmw', 'general motors', 'tesla', 'mercedes benz', 'audi']
# cars.reverse() # Bu funksiya ro'yxatni oxiridan boshiga qarab chiqaradi.
# print(cars)

# print(len(cars)) # len() funksiyasi elementlarni uzunligini chiqaradi.

# RANGE VA QADAM

# juft_sonlar = list(range(0,20,2))
# toq_sonlar = list(range(1,20,2))
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# MIN() MAX() SUM()
# narhlar = [12000, 15000, 9000, 18000, 20000]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Arzoni ", arzon, "\nQimmati ", qimmat, "\nJami ", jami)

# RO'YXATNI KESISH

# print(cars[0:3]) # Bunda ro'yxatni 0-indeksidan 3-indeksigacha kesadi.
# print(cars[:4]) # Bunda ro'yxatni 0-indeksidan 4-indeksigacha kesadi.
# print(cars[2:]) # Bunda ro'yxatni 2-indeksidan oxirigacha kesadi.

# RO'YXATDAN NUSXA OLISH

# my_cars = cars[:] # Ro'yxatdan shunday holatda nusxa olish kerak.Shunda asl ro'yxatdagi qiymatlar o'zgarmaydi.
# my_cars.remove('bmw')
# print(my_cars)
# print(cars)

# TUPLES "O'ZGARMAS RO'YXAT"

# toys = ('car', 'dimo', 'bear', 'snake') # Bunday ro'yxatga o'zgartirish kiritish uchun, buni oddiy ro'yxatga
# # aylantirib olishimiz kerak bo'ladi.Buning uchun:
# toys = list(toys)
# toys.append('teddy')
# toys.remove('car')
# print(toys)
#
# # O'zgarmas ro'yxatni o'z holiga qaytarish uchun:
# toys = tuple(toys) # shunday qilamiz.

# 9-DARS FOR LOOP ---------------------

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Sarvar']
# for mehmon in mehmonlar:
#     print("Salom ", mehmon)

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Sarvar']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon} sizni 17-may kuni nahorgi oshga taklif etamiz.")
#     print("Hurmat bilan palonchiyevlar oilasi.\n")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = []
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting: "))
# print(dostlar)

# 10-DARS:  TARMOQLANISH------------------

# avtolar = ['audi', 'bmw', 'tesla', 'volvo', 'gm']
# for avto in avtolar:
#     print(avto.title())

# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# ism = input("Ismingizni nima?\n>>>")
# if ism.lower() != 'ali':
#     print(f"Uzr {ism.title()} biz Alini kutyapmiz")
# else:
#     print("Assalomu alaykum ", ism.title())

# yosh = int(input("Yoshingiz nechada?\n>>>"))
# if yosh >= 18:
#     print("Xush kelibsiz")
# else:
#     print("Sizga kirish mumkin emas")

# login = input("Yangi login kiriting: ")
# if len(login) <= 5:
#     print("Iltimos 5 tadan ko'proq belgi kiriting!")
# else:
#     print("Login muvaffaqiyatli qabul qilindi.")

# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh = 2023-yil
# if yosh <= 18:
#     print(f"Siz endigina {yosh} yoshda ekansiz.")
#     print("Sizga kirish hozircha mumkin emas!")
# else:
#     print("Xush kelibsiz")

# x, y = 50, 60
# print("x<y") if x<y else print("x>y") # Agar kod qisqa bo'lsa, ana shunday qilib kodni bir qatorda yozishimiz mumkin.

# 10-dars uchun amaliyot
#-----------------------------------------------------

# avtolar = ['audi', 'bmw', 'tesla', 'volvo', 'gm']
# for avto in avtolar:
#     if avto == 'gm':
#         print(avto.upper())
#     else:
#         print(avto.title())


# avtolar = ['audi', 'bmw', 'tesla', 'volvo', 'gm']
# for avto in avtolar:
#     if avto != 'gm':
#         print(avto.title())
#     else:
#         print(avto.upper())


# user = input("Loginingizni kiriting: ")
# if user.lower() == 'admin':
#     print(f"Xush kelibsiz {user.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {user.title()}!")


# print("Ikkita son kiriting:")
# number = float(input("1-sonni kiriting:"))
# number2 = float(input("2-sonni kiriting:"))
# if number == number2:
#     print("Sonlar o'zaro teng ekan.")


# user = float(input("Istalgan son kiriting:"))
# if user < 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")

# son = float(input("Istalgan son kiriting: "))
# print(son**(1/2)) if son > 0 else print("Musbat son kiriting")




# 11-DARS IF ELIF ELSE-------------------

# yosh = int(input("Yoshingiz nechida? "))
# if yosh <= 4:
#     print("Sizga kirish bepul")
# elif yosh <= 12:
#     print("Sizga kirish 5000 so'm")
# else:
#     print("Sizga kirish 10000 so'm")

# yosh = int(input("Yoshingiz nechida? "))
# if yosh <= 4:
#     narh = 0
# elif yosh <= 12:
#     narh = 5000
# elif yosh <= 18:
#     narh = 8000
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} so'm")

# kun = input("Bugun qanday kun?>>>")
# if kun.lower()== 'shanba' or kun.lower()== 'yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")

# kun = input("Bugun nima kun?>>>")
# harorat = float(input("Havo harorati qanday?>>>"))
# if kun.lower()== 'yakshanba' and harorat >= 30:
#     print("Cho'milgan ketdik")
# elif kun.lower()== 'yakshanba' and harorat < 30:
#     print("Uyda dam olamiz.")

# kun = input("Bugun nima kun?>>>")
# harorat = float(input("Havo harorati qanday?>>>"))
# if (kun.lower()== 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30:
#     print("Cho'milgan ketdik")
# elif (kun.lower()== 'yakshanba' or kun.lower() == 'shanba') and harorat < 30:
#     print("Uyda dam olamiz.")


# BOOLEAN MANTIQIY OPERATORLAR
# narh = 15000
# choy = True
# non = True
# salat = False
# assorti = True
#
# if choy:
#     print("Mijoz choy oldi")
#     narh = narh + 3000
# if non:
#     print("Mijoz non oldi")
#     narh = narh + 4000
# if salat:
#     print("Mijoz salat olmadi")
#     narh = narh + 10000
# if assorti:
#     print("Mijoz assorti oldi")
#     narh = narh + 15000
# print(f"Jami {narh} so'm")

# menu = ['osh', 'manti', 'somsa', 'mastava', 'shashlik']
# user = input("Nima ovqat yeysiz? ")
# if user.lower() in menu:
#     print("Buyurtma qabul qilindi!")
# else:
#     print("Afsuski bizda bunday ovqat yo'q.")

# menu = ['osh', 'manti', 'somsa', 'mastava', 'shashlik']
# buyurtmalar = ['osh', 'chuchvara', 'norin', 'shashlik']
#
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz menuda {taom} yo'q")
# else:
#     print("Savatchangiz bo'sh")

# 11-dars uchun amaliyot
# --------------------------------------------------
# user = int(input("Juft son kiriting: "))
# if user % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Iltimos juft son kiriting.")


# user = int(input("Yoshingiz kiriting: "))
# if user <= 4 or user >= 60:
#     narh = 0
# elif user < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Sizga kirish {narh} so'm")


# print("ikkita son kiriting:")
# num1 = float(input("1-sonni kiriting:"))
# num2 = float(input("2-sonni kiriting:"))

# if num1 > num2:
#     print(f"{num1}>{num2}")
# elif num1 < num2:
#     print(f"{num1}<{num2}")
# else:
#     print("Kiritgan sonlaringiz teng.")

# print("Kamida 5 ta mahsulot nomini kiriting:")
# mahsulotlar = ['anor', 'olma', 'shaftoli', 'nok', 'non', 'uzum', 'un', "yog'", 'shakar', 'sut']
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni kiriting: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")


# mahsulotlar = ['anor', 'olma', 'shaftoli', 'nok', 'non', 'uzum', 'un', "yog'", 'shakar', 'sut']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print(f"Siz so'ragan barcha mahsulotlar do'konimizda bor.")


# foydalanuvchilar = ['anvar', 'sarvar', 'azimjon', 'sardor', 'umidjon']
# foydalanuvchi = input("Yangi login tanlang: ")
# if foydalanuvchi in foydalanuvchilar:
#     print('login  band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {foydalanuvchi.title()}!")

# user = int(input("Istalgan butun sonni kiriting: "))
# for n in range(2,11):
#     if user % n == 0:
#         print(f"{user} soni {n} ga qoldiqsiz bo'linadi.")


# ----------------------------------------------------

# 14-DARS: Dictionary (Lug'at)

# car_0 = {'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# talaba_0 = {'ism':'sarvarbek xalilov', 'yosh':25, 't_yil':1998}
# print(f"{talaba_0['ism'].title()},\
#    {talaba_0['t_yil']} yil , {talaba_0['yosh']} yoshda")
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# print(talaba_0)

# talaba_0 = {}
# talaba_0['kurs'] = 3
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'sarvarbek'
# print(f"{talaba_0['ism'].title()}, {talaba_0['fakultet']} fakultetining \
# {talaba_0['kurs']}-kurs talabasi")

# 14-dars amaliyoti

otam = {'ism':'odiljon', 't_yil':1971, 'kasb':'nonvoy'}
print(f"Otamning ismi {otam['ism'].title()} {otam['t_yil']}\
-yilda tug'ilgan, kasblari {otam['kasb']}.")

#------------------------------------------

sevimli_taom = {'anvar':'osh', 'sarvar':'moshkichiri', 'ravshan': 'manti', 'nozim':'shavla'}
print(f"Anvarning sevimli taomi {sevimli_taom['anvar']}\n\
Sarvarning sevimli taomi {sevimli_taom['sarvar']}\n\
Nozimning sevimli taomi {sevimli_taom['nozim']}")

#-------------------------------------------

py_lt = {
    'integer':'butun son',
    'float':'o\'nlik son',
    'string':'matn',
    'if':'agar',
    'else':'aks holda',
    'for':'uchun',
    'elif':'aks holda agar',
    'print':'chop etmoq'
}
# print(f"pythonda hozirgacha o'rgangan metodlarim {py_lt}")

# print(py_lt.get(user,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting: ").lower()
tarjima = py_lt.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas!")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi.")
