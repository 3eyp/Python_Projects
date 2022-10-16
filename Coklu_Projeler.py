
import datetime
import pandas as pd
import random
import time
import math

import colorama
colorama.init()

from PIL import Image


class Question():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def chackAnswer(self,answer):
        return self.answer==answer
class Quiz():
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestions(self):
        return self.questions[self.questionIndex]

    def displayQuestions(self):
        question=self.getQuestions()
        print(f"Soru {self.questionIndex+1}: {question.text}")
        for q in question.choices:
            print("-",q)
        answer=input("Cevap: ")
        self.quess(answer)
        self.loadQuestions()
    def quess(self,answer):
        question = self.getQuestions()
        if question.chackAnswer(answer):
            self.score+=1
        self.questionIndex+=1
    def loadQuestions(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
            self.displayProgres()
        else:
            self.displayProgres()
            self.displayQuestions()
    def showScore(self):
        print(colorama.Fore.BLUE,f"  {self.questionIndex} sorudan  {self.score} adet doğru cevapladınız ... ".center(70,"$"))
    def displayProgres(self):
        textNumber=len(self.questions)
        IndexNum=self.questionIndex+1
        if IndexNum>textNumber:
            print(colorama.Fore.MAGENTA," ...QUİZ BİTTİ... ".center(100))
        else:
            print("  {} Sorudan {}. Soru  ".format(textNumber,IndexNum).center(70,"*"))

q1=Question("Aşağıdaki programın ekrana vereceği çıktı nedir?\nA=2     B=5\nc=b**a\nd=a+b+c\nprint(d)",["5".strip(),"25".strip(),"30".strip(),"32".strip()],"32")
q2=Question("Aşağıdakilerden hangisi değişken ismi olarak kullanılabilir?",["1sayı".strip(),"sayi1".strip(),"1incisayı".strip(),"birinci.sayı".strip()],"sayi1")
q3=Question("liste[:]=[] komutunun görevi aşağıdakilerden hangisidir?",["Listede kaç elaman olduğunu, karakter sayısını vb. verir".strip(),"Liste oluşturmayı sağlar".strip(),"Listeye yeni eleman eklemeyi sağlar".strip(),"Listedeki bütün elemanları silmeyi sağlar".strip()],"Listedeki bütün elemanları silmeyi sağlar")
q4=Question(" Metinsel bir ifadeyi Sayısal bir ifadeye çevirmek için hangi komutu kullanırız?",["Str()".strip(),"İnt()".strip(),"Float()".strip(),"Numeric()".strip()],"İnt()")
q5=Question(" Aşağıdakilerden hangisi kaçış dizisi sembolüdür?",["?".strip(),"#".strip(),"/".strip(),"-".strip()],"/")
q6=Question("merhaba benim adım mesut\ncümlesini hangi kod ile:\n-hepsini büyük yapabiliriz.\n-sadece ilk hafrini büyük yapabiliriz",["lower(),upper()".strip(),"capitalize(),lower()".strip(),"upper(),big()".strip(),"upper(),capitalize()".strip()],"upper(),capitalize()")
q7=Question("fonksiyon oluşturmak için hangi kodu kullanmamız gerekir?",["for".strip(),"if,elif,else".strip(),"while".strip(),"def".strip()],"def")
q8=Question("Aşağıdaki ifadelerden hngisi doğru ifadedir?",["if x>y class:".strip(),"while true".strip(),"for y range(10)".strip(),"if a==b:".strip()],"if a==b:")
q9=Question("a=Hello\nb=word\nprint(a+b)\nyukarıdaki ifadenin çıktısı nedir?",["hello word".strip(),"Hello word".strip(),"Helloword".strip(),"helloword".strip()],"Helloword")
q10=Question("for i in range(10,1,-1)\nif i%2==0:\n   continue\nelse:\nprint(i)\nifadesinin çıktısı hangisidir?",["2,4,6,8".strip(),"3,5,7,9".strip(),"9,7,5,3,1".strip(),"9,7,5,3".strip()],"9,7,5,3")
q11=Question("Aşağıda verilen değişken ismi ve değerlerinden hangisi doğru tanımlanmıştır?",["Okul numarası='47100012'","dogumYeri='Çorum'","OgrenciAdi=Pınar","Doğum yılı=1999","%basarisi=70"],"dogumYeri='Çorum'")
q12=Question("Aşağıda verilen veri türü ve eşleştirmelerden hangisi yanlıştır?",["kilo=80 (tam sayı- integer)","sehir='Çorum' (Karakter dizisi - string)","Ad='Monty' (Dizi - char)","sayi=19 (Tam sayı- integer)","ortalama=75.8 (Ondalıklı sayı - float)"],"Ad='Monty' (Dizi - char)")
q13=Question("dictionary simgesi hangisidir?",["{}","[]","()","::"],"{}")
q14=Question("sehirler={'İstanbul':'34','Bingöl':'12','Ankara':'6','Kocaeli':'41'}\n3. karakterdeki ilin plakasının print ile yazdırılması için hangi komut gereklidir?",["print('41')","print('sehirler[3]')","print('Kocaeli')","print('Ankara[1]')"],"print('Kocaeli')")
q15=Question("Aşağıdakilerden hangisinde doğru fonksiyon kullanımı vardır?",["A) def toplama\n   return a+b","B) def 1adetislem(a,b):\n   return a+b","C) def carpma(a,b);\n   return a*b","D) def bolme(a,b):\n   return a//b"],"D")

questions=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15]
questions = Quiz(questions)


print(colorama.Fore.LIGHTGREEN_EX + "\n"+"  *************** BİLGİ VE İSTATİSTİK ÇALIŞMASI *************** ".center(116)+"\n")
while True:
    time.sleep(1.5)
    print(colorama.Fore.RED+" == ALANLAR == \n".center(115))
    print(colorama.Fore.YELLOW+f"MENÜ-1 = SU Bilimi{'MENÜ-4 = Hesap makinesi'.center(81)}{'MENÜ-7 = Sayı Tahmin Oyunu'}\n{colorama.Fore.YELLOW+'MENÜ-2 = Youtube İstatistikleri'}{'MENÜ-5 = --SINAV--'.center(50)}{'MENÜ-8 = Not Yaz'.center(51)}\n{'MENÜ-3 = Arka plan şeffaf yapma'}{'MENÜ-6 = Yaş ve Emeklilik Hesabı'.center(63)}{colorama.Fore.RED+'MENÜ-9/q = --ÇIKIŞ-- '.center(31)}")
    print(colorama.Fore.LIGHTCYAN_EX+"\nİşelminize hangi alanda devam edilsin? (1/2/3/4/5/6/7/8/9-q)")
    islem =input("Seçiminiz: ")
    if islem=="1":
        class Su_bolumu:
            def temel(self):
                with open("su.txt", "r", encoding="UTF-8") as file:
                    print(colorama.Fore.MAGENTA, file.read())
            def detaybilgi(self):
                with open("su_detay.txt", "r", encoding="UTF-8") as file1:
                    print(colorama.Fore.GREEN, file1.read())
        while True:
            a1 = Su_bolumu()
            print(colorama.Fore.RED, f"{'=KONU BAŞLIKLARI='.center(60)}")
            print(f"{colorama.Fore.BLUE+'-TEMEL BİLGİLER'.center(20)}{colorama.Fore.BLUE+'-DETAYLI BİLGİ'.center(40)}\n ")
            print(f"{colorama.Fore.YELLOW+'temel bilgiler   - 1'}\ndetaylı bilgiler - 2{colorama.Fore.RED+'Ana Menü(Geri)-q'.center(40)}\n")
            secim=input("Seçiminiz:")
            if secim=="1":
                a1.temel()
            elif secim=="2":
                a1.detaybilgi()
            elif secim=="q":
                print(colorama.Fore.RED+"Ana menüye aktarılıyorsunuz...")
                time.sleep(1)
                break
            else:
                print(colorama.Fore.RED,"=Hatalı Seçim=".center(12))
                continue
    elif islem=="2":
        class YoutubeIstatistic():
            def istatistikler(self):
                df = pd.read_csv("GBvideos.csv")
                while True:
                    print(colorama.Fore.CYAN,f"\n{' =MENÜ= '.center(115)}\n\nYoutube istatistik bilgileri = 1{'Youtube En çok izlenen Video = 2'.center(62)}{'Youtube En çok Beğenilen ilk 10 Video = 3'}\n{'Youtube Beğeni ortalaması = 4'}{'Hepsi = 6'.center(45)}{colorama.Fore.RED+'Ana Menü(GERİ) = 5/q'.center(59)}\n")
                    soru = input("Seçiminiz:")
                    if soru == "1":
                        print(colorama.Fore.RESET, df.info)
                    elif soru == "2":
                        print(colorama.Fore.RED + f"En çok izlenen video = {df['views'].max()}\nVideo Adı =",df[["views", "title"]].sort_values("views", ascending=False).head(1)["title"])
                    elif soru == "3":
                        print(colorama.Fore.GREEN + df.sort_values("likes", ascending=False).head(10)["title"])
                    elif soru == "4":
                        print(colorama.Fore.RED + "Beğeni ortalaması =" + str(df.likes.mean()))
                    elif soru == "5" or soru=="q":
                        print(colorama.Fore.RED+" ...Çıkış Sağlanyor...")
                        time.sleep(1)
                        break
                    elif soru == "6":
                        print("*******************************************************************************")
                        print(colorama.Fore.GREEN + f"İstatistikler ve Bilgiler:\n\nKolon sayısı={len(df.columns)}\n***********\nSütun sayısı:{len(df.title)}\n**********\nKolon Adları:{df.columns}\n*************\nEn çok izlenen video:{df.views.max()}\n*****************\nEn çok beğenilen video:{df['likes'].max()}")
                    else:
                        print(colorama.Fore.RED + " ---- HATALI SEÇİM ---- ".center(10, "*"))
                        continue
        istatik = YoutubeIstatistic()
        istatik.istatistikler()
    elif islem=="3":

        def convertImage():
            img = Image.open("örn.png")     # Bu alana şeffaf yapmak istediğiniz image ekleyiniz
            img = img.convert("RGBA")

            datas = img.getdata()

            newData = []

            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)
            img.save("seffafYapılanResim.png", "PNG") # Bu alana şeffaf olacak resim için png uzantılı dosya açınız
            print("Successful")
        print(colorama.Fore.RED+"\n    Bu işlemde kopyala yapıştır yolunu deneyiniz \n")

    elif islem=="4":
        def islem(args):
            def hesapmakinesi(*argss, **kwargs):
                simdi = time.time()
                time.sleep(1)
                result = args(*argss, **kwargs)
                bitis = time.time()
                print(colorama.Fore.YELLOW + f"{args.__name__} İşlemi Sonucunuz: {bitis - simdi} sn. sürdü.")
                print(colorama.Fore.RED + "SONUÇ =", result)
            return hesapmakinesi
        class Hesap():
            @islem
            def toplama(self, a, b):
                return a + b
            @islem
            def cikarma(self, a, b):
                return a - b
            @islem
            def carpma(self, a, b):
                return a * b
            @islem
            def bolme(self, a, b):
                return a / b
            @islem
            def faktoriyel(self, a):
                return math.factorial(a)
            @islem
            def usalma(self, a, b):
                return a ** b
        a = Hesap()
        while True:
            print(colorama.Fore.YELLOW + " = HESAP MAKİNESİ =".center(90))
            print(colorama.Fore.BLUE + f"\n-Toplama = +{'-Çıkarma = -'.center(40)} {'-Çarpma = *'.center(20)}\n{'- Bölme = /'} {'-Üs Alma = **'.center(40)} {'-Çıkış = q'.center(15)}")

            sayi1 = int(input("\n1. Sayı:"))
            sayi2 = int(input("2. Sayı:"))

            secenek=input("+ | - | * | / | ** | =")

            if secenek == "toplama" or secenek == "Toplama" or secenek=="+":
                a.toplama(sayi1,sayi2)
                break
            elif secenek == "çıkarma" or secenek == "Çıkarma" or secenek=="-":
                a.cikarma(sayi1, sayi2)
                break
            elif secenek == "çarpma" or secenek == "Çarpma" or secenek=="*":
                a.carpma(sayi1, sayi2)
                break
            elif secenek == "bölme" or secenek == "Bölme" or secenek=="/":
                a.bolme(sayi1, sayi2)
                break
            elif secenek == "üs alma" or secenek == "Üs alma" or secenek=="**":
                a.usalma(sayi1, sayi2)
                break
            else:
                print(colorama.Fore.RED+" *** HATALI İŞLEM *** ".center(15))
                break
    elif islem=="5":
        class Sinav():
            def sinav(self):
                print(colorama.Fore.LIGHTYELLOW_EX, "==DİKKAT==".center(80))
                print("CEVAP VERECEĞİNİZ ZAMAN ŞIKLARDAN DOĞRU OLARAK TAHMİN ETTİĞİNİZİ KOPYALA YAPIŞTIR İLE CEVAPLAYINIZ\nEN ÖNEMLİSİ İSE BAŞINA VE SONUA BOŞLUK EKLEMEMENİZ LAZIM ÇÜNKÜ;\nDOĞRU DAHİ OLSA BOŞLUK HASSASİYETİNDEN DOLAYI YANLIŞ KABUL EDER\nSADECE 15. SORUDA ŞIKLARIN İSMİ VARDIR VE HANGİSİNİN DOĞRU OLDUĞUNU DÜŞÜNÜYORSANIZ O ŞIK HARFİNİ BÜYÜK HARF İLE YAZINIZ\nBAŞARILAR DİLERİM...")
                colorama.init()
                print(colorama.Fore.LIGHTGREEN_EX)
                questions.loadQuestions()
        s = Sinav()
        s.sinav()
    elif islem=="9" or islem=="q":
        print(colorama.Fore.MAGENTA,"...Çıkış yapılıyor...".center(10))
        time.sleep(2)
        break
    elif islem=="6":
        print(colorama.Fore.BLUE+f"{  '= EMEKLİLİK VE YAŞ HESAPLAMA = '.center(80)}")
        name = input("Adınız : ")
        dogumyili = int(input("Doğum yılınız: ÖRN(1978) ="))
        def yas(func):
            def sene(yil):
                simdi = datetime.datetime.now().year
                result = simdi - yil
                emeklilik=65-result
                func(yil)
                while True:
                    print(colorama.Fore.YELLOW+"\n = EMEKLİLİK VE YAŞ HESAPLAMA = ")
                    print(f"\n{'Yaş Hesapla -1'}\n{'Emeklilik Hesapla -2'}\n{'Yaş Ve Emeklilik hesabı -3'}\n{colorama.Fore.RED + 'Çıkış -q'}\n")
                    secimler = input("Seçeneğiniz = ")
                    if secimler == "q":
                        print(colorama.Fore.MAGENTA+"\nİşlemden Çıkılıyor... ".center(20))
                        time.sleep(1)
                        break
                    else:
                        if secimler=="1":
                            print(colorama.Fore.BLUE+f"\nMerhaba {name.upper()} Yaşınız: {result}")
                        elif secimler=="2":
                            if 65 - result > result:
                                print(colorama.Fore.BLUE+f"Emeklilik Hesap = Emekliliğinize : {emeklilik} yıl kaldı.",colorama.Fore.LIGHTGREEN_EX + 'NOT = Emeklilik hesabı 65 yaşa göre yapılmaktadır...'.center(55))
                            elif 65 == result:
                                print(colorama.Fore.BLUE+f"Emeklilik Hesap = Bu sene emekli oldunuz...",colorama.Fore.LIGHTGREEN_EX + 'NOT = Emeklilik hesabı 65 yaşa göre yapılmaktadır...'.center(55))
                            else:
                                print(colorama.Fore.BLUE+f"Emeklilik Hesap = {result - 65} yıl önce emekli oldunuz. " + colorama.Fore.LIGHTGREEN_EX + 'NOT = Emeklilik hesabı 65 yaşa göre yapılmaktadır...'.center(55))
                        elif secimler=="3":
                            if 65 - result > result:
                                print(colorama.Fore.BLUE+f"Merhaba {name.upper()} Yaşınız: {result}\nEmeklilik Hesap = Emekliliğinize : {emeklilik} yıl kaldı.",colorama.Fore.LIGHTGREEN_EX + 'NOT = Emeklilik hesabı 65 yaşa göre yapılmaktadır...'.center(55))
                            elif 65 == result:
                                print(colorama.Fore.BLUE+f"Merhaba {name.upper()} Yaşınız: {result}\nEmeklilik Hesap = Bu sene emekli oldunuz...",colorama.Fore.LIGHTGREEN_EX + 'NOT = Emeklilik hesabı 65 yaşa göre yapılmaktadır...'.center(55))
                            else:
                                print(colorama.Fore.BLUE+f"Merhaba {name.upper()} Yaşınız: {result}\nEmeklilik Hesap = {result - 65} yıl önce emekli oldunuz. " + colorama.Fore.LIGHTGREEN_EX + 'NOT = Emeklilik hesabı 65 yaşa göre yapılmaktadır...'.center(55))
                        else:
                            print(colorama.Fore.RED," ...HATALI SEÇİM... ".center(20))
            return sene
        @yas
        def yasHesapla(dogum):
            return dogum
        yasHesapla(dogumyili)
        
        class Not():
            def yaz(self):
                result = input("\n ...Notlarım... \n")
                with open("notlarim.txt", "a", encoding="UTF-8") as file:
                    file.write(result)

            def oku(self):
                with open("notlarim.txt", encoding="UTF-8") as file:
                    print(f"{colorama.Fore.RED + ' === Notlarınız ==='.center(90)}\n")
                    print(colorama.Fore.YELLOW + file.read())
        n = Not()
    elif islem=="8":
        print((f"{colorama.Fore.GREEN + ' =MENÜ= '.center(90)}\n{colorama.Fore.YELLOW + 'Not Yaz -1'}\n{colorama.Fore.YELLOW + 'Notlarımı Oku -2'}\n{colorama.Fore.RED+'Çıkış -q'}\n"))
        sec = input(f"Seçiminiz = ")
        if sec == "1":
            with open("notlarim.txt","w",encoding="UTF-8") as file2:
                result=input("Notlarım =  ")
                file2.write(f"\n{'-'}{ result}")
        elif sec == "2":
            with open("notlarim.txt",encoding="UTF-8") as file4:
                print(colorama.Fore.RED,"... Notlarınız ...".center(50))
                print(colorama.Fore.GREEN,file4.read())
        while True:
                import colorama
                print((f"\n{colorama.Fore.GREEN+'=MENÜ='.center(90)}\n{colorama.Fore.YELLOW+'Not Yaz,Devam -1'}\n{colorama.Fore.YELLOW+'Notlarımı Oku -2'}\n{colorama.Fore.RED+'Çıkış -q'}\n"))
                sec = input(f"Seçiminiz = ")
                if sec=="2":
                    with open("notlarim.txt",encoding="UTF-8") as file3:
                        print(colorama.Fore.RED+f"{' =Notlatınız = '.center(90)}")
                        print(colorama.Fore.YELLOW+f"{file3.read()}")
                elif sec=="q":
                    print(colorama.Fore.MAGENTA,"Ana menüye aktarılıyorsunuz...")
                    time.sleep(1)
                    break
                elif sec=="1":
                    with open("notlarim.txt","a",encoding="UTF-8") as file:
                        ekle=input("Not devam:\n")
                        file.write(f"\n{'-'}{ ekle}")
                else:
                    print(" ... Hatalı Seçim ... ")
                    continue
    elif islem=="7":
        print(colorama.Fore.MAGENTA + " Menü \n".center(100))
        print("1-) 1 ile 10 arasında oyun\n2-) 1 ile 100 arasında oyun\n3-) 10 ile 1000 arasında oyun\n")
        secimSayiTahmin = input(colorama.Fore.YELLOW + "\nSeçiminiz : ")

        if secimSayiTahmin == "1":
            print(
                colorama.Fore.GREEN + f"\n1 ile 10 arasında sayı tahminleri için {colorama.Fore.RED + str(3)} {colorama.Fore.GREEN + 'hakkınız mevcut olacaktır...'}\n".center(
                    100))
            sayi = random.randint(1, 10)

            sayac = 0

            while sayac < 3:
                sayac += 1
                tahmin = int(input(colorama.Fore.BLUE + f"{sayac}. Tahmininiz : "))

                if tahmin == sayi:
                    print(f"\ntebrikler tutulan sayı {sayi}\n{colorama.Fore.RED + str(sayac)}. defada bildiniz.\n")
                    break
                elif tahmin > sayi:
                    print(colorama.Fore.MAGENTA + "Aşağı.")
                elif tahmin < sayi:
                    print(colorama.Fore.GREEN + "Yukarı.")
                else:
                    print(colorama.Fore.RED + "hata...")

                if sayac == 3:
                    print(
                        f"{colorama.Fore.YELLOW + 'Hakkınız bitti tutulan sayı'} {colorama.Fore.RED + str(sayi)} {colorama.Fore.GREEN + 'tekrar deneyiniz...'}")



        elif secimSayiTahmin == "2":
            print(
                colorama.Fore.GREEN + f"\n1 ile 100 arasında sayı tahminleri için {colorama.Fore.RED + str(5)} {colorama.Fore.GREEN + 'hakkınız mevcut olacaktır...'}\n".center(
                    100))
            sayi = random.randint(1, 100)

            sayac = 0

            while sayac < 5:

                sayac += 1
                tahmin = int(input(colorama.Fore.BLUE + f"{sayac}. Tahmininiz : "))

                if tahmin == sayi:
                    print(f"tebrikler tutulan sayı {sayi}\n{colorama.Fore.RED + str(sayac)}. defada bildiniz.\n")
                    break
                elif tahmin > sayi:
                    print(colorama.Fore.MAGENTA + "Aşağı.")
                elif tahmin < sayi:
                    print(colorama.Fore.GREEN + "Yukarı.")
                else:
                    print(colorama.Fore.RED + "hata...")

                if sayac == 5:
                    print(
                        f"{colorama.Fore.YELLOW + 'Hakkınız bitti tutulan sayı:'} {colorama.Fore.RED + str(sayi)} {colorama.Fore.GREEN + 'tekrar deneyiniz...'}")


        elif secimSayiTahmin == "3":

            print(
                colorama.Fore.GREEN + f"\n10 ile 1000 arasında sayı tahminleri için {colorama.Fore.RED + str(7)} {colorama.Fore.GREEN + 'hakkınız mevcut olacaktır...'}\n".center(
                    100))
            sayi = random.randint(10, 1000)

            sayac = 0

            while sayac < 7:

                sayac += 1

                tahmin = int(input(colorama.Fore.BLUE + f"{sayac}. Tahmininiz : "))

                if tahmin == sayi:
                    print(f"tebrikler tutulan sayı {sayi}\n{colorama.Fore.RED + str(sayac)}. defada bildiniz.\n")
                    break
                elif tahmin > sayi:
                    print(colorama.Fore.MAGENTA + "Aşağı.")
                elif tahmin < sayi:
                    print(colorama.Fore.GREEN + "Yukarı.")
                else:
                    print(colorama.Fore.RED + "hata...")

                if sayac == 7:
                    print(f"{colorama.Fore.YELLOW + 'Hakkınız bitti tutulan sayı'} {colorama.Fore.RED + str(sayi)} {colorama.Fore.GREEN + 'tekrar deneyiniz...'}")


    else:
        print(colorama.Fore.RED+"\nHatalı seçim...")