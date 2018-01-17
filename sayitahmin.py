import random
import time

print("""**************************
Sayı Tahmin Oyunu
1 ile 20 arasında sayı tahmini yapın..
5 Hakkınız var..
**************************""")

tahmin_hakki=5
random=random.randint(1,20)
while True:
    sayi=int(input("Sayıyı Tahmin Edin :"))
    if sayi <random:
        print("Tahmininz kontrol ediliyor...")
        time.sleep(1)
        print("Daha yüksek bir sayi tahmin edin")
        tahmin_hakki -=1
    elif sayi>random:
        print("Tahmininiz Kontrol Ediliyor...")
        time.sleep(1)
        print("Daha düşük bir sayı tahmin edin")
        tahmin_hakki-=1
    else:
        print("Tebrikler Doğru Bildiniz =",random)
        break

    if tahmin_hakki==0:
        print("Tahmin Hakkınız Doldu ! Bilemediniz!","Doğru sayı =",random)
        break