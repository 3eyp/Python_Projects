
#Yazdığımız bir python uygulamasındaki belli bir kod parçasını bir kaç yerde kullanma ihtiyacı duyduğumuzda fonksiyon oluşturmak işlerimizi kolaylaştırır.
# Böyle durumlarda sürekli kullanacak olduğumuz kod satırlarını fonksiyonlar içine alıp istediğimiz zaman çağırıp çalıştırabiliriz.



def myFunction():
    print("Merhaba")

myFunction()



# def fonksiyonunda return değer döndürme metodu.

def myFunctions():
    return "merhaba"

result=myFunctions()
print(result)



# def fonksiyonu return değer print ile değişkensiz yazdırma metodu.

def myPrint():
    return "merhaba"

print(myPrint())

