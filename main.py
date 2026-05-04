
# 3-m
class Bankhisob:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.__balans = balans

    def pul_qosh(self, summa):
        self.__balans += summa

    def pul_yech(self, summa):
        self.__balans -= summa

    def info(self):
        print(f"Egasi: {self.egasi}")
        print(f"Balans: {self.__balans}")

b1 = Bankhisob("Ali", 10000)
b1.info()

b1.pul_qosh(10000)
b1.info()

b1.pul_yech(1000)
b1.info()


# 4-m
class Telefon:
    def __init__(self, madel, batareya):
        self.madel = madel
        self.__batareya = batareya

    def zaryad_qil(self, foiz):
        self.__batareya == foiz

    def foydalan(self, foiz):
        self.__batareya == foiz

    def info(self):
        print(f"Madeli: {self.madel}")
        print(f"Batareya: {self.__batareya}")

t1 = Telefon("iPhone", '50%')
t1.info()

t1.zaryad_qil(1)
t1.info()

t1.foydalan(100)
t1.info()
