class Bicycle:
    def run(self,km):
        print("骑行里程数为",km)
class EBicycle(Bicycle):
    def __init__(self,valume):
        self.valume = valume
    def get_valume(self):
        print("当前电量为",self.valume)
    def fill_charge(self,vol):
        print("充电的电量为",vol)
    def run(self,km):
        emiles = self.valume*10
        miles = km - emiles
        if miles <= 0 :
            print("电动车行驶的里程数为",km)
        else:
            print("电动车行驶的里程数为",emiles)
            super().run(miles)

ebicycle = EBicycle(10)
ebicycle.run(150)
