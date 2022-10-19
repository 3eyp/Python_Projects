import time
import colorama
colorama.init()

class MyDecorator():
    def islem(args):
        def hesapmakinesi(*argss, **kwargs):
            simdi = time.time()
            time.sleep(1)
            result = args(*argss, **kwargs)
            bitis = time.time()
            print(colorama.Fore.RED + f"\n{args.__name__} İşlemi Sonucunuz : {colorama.Fore.BLUE+str(bitis - simdi)} sn. sürdü.")
            print(colorama.Fore.GREEN + "SONUÇ =",str(result)+"\n")
        return hesapmakinesi

    @islem
    def toplama():
        return 5+5

    toplama()

    @islem
    def cikarma():
        return 7-3

    cikarma()


MyDecorator()



