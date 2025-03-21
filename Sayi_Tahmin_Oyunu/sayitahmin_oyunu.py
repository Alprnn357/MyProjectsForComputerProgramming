import sys
import os
import time
import random

oyuncuAdi = "Oyuncu"

def isimOku():
    global oyuncuAdi
    saveFile = open("sayitahmin_oyunu_data.txt","r")
    oyuncuAdi = saveFile.readline()
    saveFile.close()

def isimDegistir():
    global oyuncuAdi
    clear()
    print("Oyuncu isminizi giriniz.")
    oyuncuAdi = input("İsim: ")
    saveFile = open("sayitahmin_oyunu_data.txt","w")
    saveFile.write(oyuncuAdi)
    saveFile.close()
    isimOku()

def clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def oyun():
    gercekSayi = random.randrange(1,100,1)
    oyunGirdi = 0

    clear()
    print("Oyun başladı!")
    while True:
        print("Sayıyı tahmin ediniz (1-100).")
        oyunGirdi = input("Girdi: ")

        try:
            oyunGirdi = int(oyunGirdi)
        except:
            clear()
            print("Yanlış argüman, lütfen 1 ile 100 arasında bir sayı yazınız.")
            continue

        if oyunGirdi == gercekSayi:
            clear()
            print("TEBRİKLER SAYIYI BULDUN!")
            time.sleep(2)
            break
        elif abs(oyunGirdi - gercekSayi) <= 5:
            clear()
            print("ÇOK SICAK!")
        elif abs(oyunGirdi - gercekSayi) <= 10:
            clear()
            print("Sıcak")
        elif abs(oyunGirdi - gercekSayi) <= 20:
            clear()
            print("Ilık")
        elif abs(oyunGirdi - gercekSayi) <= 30:
            clear()
            print("Soğuk")
        elif abs(oyunGirdi - gercekSayi) <= 50:
            clear()
            print("Çok soğuk")
        else:
            clear()
            print("Buz gibi oldum.")
        
        
def anaMenu():
    print("SAYI TAHMİN ETME OYUNU")
    print("Hoşgeldin " + oyuncuAdi + ". 1 ile 100 arasında rastgele bir sayı üretilecek. Sen ise bu sayıyı bulmaya çalışacaksın. Soğuk mu yoksa sıcak mı sana söyleyeceğim.")
    print("1. Oyunu Başlat")
    print("2. Oyuncu ismini değiştir")
    print("0. Oyundan Çık")
    global menuGirdi
    menuGirdi = input("Girdi: ")

def main():
    global oyuncuAdi

    if os.path.exists("sayitahmin_oyunu_data.txt"):
        isimOku()
    else:
        isimDegistir()
        
    
    while True:
        clear()
        anaMenu()

        if menuGirdi == "1":
            oyun()
            continue
        if menuGirdi == "2":
            isimDegistir()
            continue
        elif menuGirdi == "0":
            clear()
            print("Oyundan çıktınız.")
            break
        else:
            clear()
            print('Yanlış girdi!')
            time.sleep(1)
            continue

main()