
#İç içe fonksiyon kullanımları;


def isim():
    return "eyüp"

def selam():

    print(f"Merhaba {isim()}")

selam()




# fonksiyona değişken tanımlama ile iç içe fonsiyon;

def isims(ad):
    return ad

def selams():

    print(f"Merhaba {isims('ali')}")

selams()

