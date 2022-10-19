import time
import colorama

class HesapMakinem():

    def __init__(self):
        self.hesap()

    def toplama(self,a,b):
        return a+b

    def cikarma(self,a,b):
        return a-b

    def carpma(self,a,b):
        return a*b

    def bolme(self,a,b):
        return a/b

    def hesap(self):
        ad=input(colorama.Fore.RED+"Ad : ")
        print(colorama.Fore.YELLOW+f"Merhaba {ad} seni aramızda görmek harika :)\n".center(100))
        time.sleep(1)

        print(" Hesap Makinem ".center(100,"*"))

        sayi1=int(input("1. Sayı : "))
        sayi2=int(input("2. Sayı : "))

        secim=input("\n+\n-\n*\n/\n\nSeçiminiz : ")

        if secim=="+":

            print(f"\nİşlem sonucunuz = {self.toplama(sayi1,sayi2)}")
        elif secim=="-":
            self.cikarma(sayi1,sayi2)
        elif secim=="*":
            self.carpma(sayi1,sayi2)
        elif secim=="/":
            self.bolme(sayi1,sayi2)
        else:
            print("Hatalı seçim...")


HesapMakinem()



