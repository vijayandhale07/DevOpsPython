class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def info(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        
        
c1 = Car("Tyota","Foutuner")

c1.info()
    