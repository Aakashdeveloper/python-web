for abc import ABC, abstractmethod

class Car(ABC)
    @abstractmethod
    def price_inc(self):
        self.price = int(self.price*1.15)

class SuperCar(Car):
    def __init__(self, modelname,yearm,price,cc):
        super.__init__(modelname,yearm,price)
        self.cc=cc

honda = SuperCar('City',2019,900000)
tata = Car('Bolt',2018,800000)

honda.cc == 1500
honda.price_inc()