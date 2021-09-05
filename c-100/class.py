class Car():
    def __init__(self,model,color,company,speedlimit):
        self.color=color
        self.model=model
        self.company=company
        self.speedlimit=speedlimit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def acceleration(self):
        print("accerlerating")
    
    def changegear(self,gear):
        print("gear changed to ",gear)
    
ferrari=Car("ferrari roma","gray","Fiat",211)
print(ferrari.model)
print(ferrari.color)
print(ferrari.company)
print(ferrari.speedlimit)
ferrari.start()
ferrari.stop()
ferrari.acceleration()
ferrari.changegear(4)

buggativeron=Car("buggati veron","blue","audi",199)
print(buggativeron.model)
print(buggativeron.color)
print(buggativeron.company)
print(buggativeron.speedlimit)
buggativeron.start()
buggativeron.stop()
buggativeron.acceleration()
buggativeron.changegear(3)