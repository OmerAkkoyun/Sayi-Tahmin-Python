import random
import time

print("""**************************
Say� Tahmin Oyunu
1 ile 20 aras�nda say� tahmini yap�n..
5 Hakk�n�z var..
**************************""")

tahmin_hakki=5
random=random.randint(1,20)
while True:
    sayi=int(input("Say�y� Tahmin Edin :"))
    if sayi <random:
        print("Tahmininz kontrol ediliyor...")
        time.sleep(1)
        print("Daha y�ksek bir sayi tahmin edin")
        tahmin_hakki -=1
    elif sayi>random:
        print("Tahmininiz Kontrol Ediliyor...")
        time.sleep(1)
        print("Daha d���k bir say� tahmin edin")
        tahmin_hakki-=1
    else:
        print("Tebrikler Do�ru Bildiniz =",random)
        break

    if tahmin_hakki==0:
        print("Tahmin Hakk�n�z Doldu ! Bilemediniz!","Do�ru say� =",random)
        break