class Car(object): 


    def __init__(self, model, color, company, speed_limit): 
        self.color = color
        self.company = company     
        self.speed_limit = speed_limit
        self.model = model  
        
    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarate...")
        "accelarator functionality here"

    def charge_gear(self, gear_types):
        print("gear changed")
        "gear related funnctionality here"


audi = Car("A6", "red", "audi", 80)

print(audi.start())
