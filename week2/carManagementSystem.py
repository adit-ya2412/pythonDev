class Engine:
    def __init__(self,engine_type,horsepower):
        self.engine_type=engine_type
        self.horsepower=horsepower

    def start_engine(self):
        return f"{self.engine_type} engine has started"
    
class Car:
     def __init__(self,brand,model,engine):
         self.brand=brand
         self.model=model
         self.engine=engine
         self.service_history=[]

     def display_info(self):

        return (
        f"{self.brand} {self.model}\n"
        f"Engine: {self.engine.engine_type}\n"
        f"Horsepower: {self.engine.horsepower}"
        )
    
     def start_car(self):
         return self.engine.start_engine()
     def change_engine(self,new_engine):
         self.engine=new_engine
         self.service_history.append(f"Engine changed to {new_engine.engine_type}")
         return f"Engine changed to {new_engine.engine_type}"
     def change_oil(self):
         self.service_history.append("Engine Oil Changed")
         return "oil changed in car successfully"

class ElectricEngine(Engine):
    def __init__(self, horsepower,battery_power):
        super().__init__("Electric", horsepower)
        self.battery_power=battery_power

    def start_engine(self):
        return f"{super().start_engine()} battery level at 100% , Battery power is {self.battery_power}kwh"


tesla=Car("Tesla","Model",ElectricEngine(190,500))

print(tesla.change_oil())
print(tesla.display_info())
print(tesla.start_car())
print(tesla.service_history)

k10=Engine("Petrol",110)

swift=Car("Suzuki","Swift VXI",k10)

print(swift.start_car())
print(swift.change_engine(Engine("Diesel"
                                 ,95)))
print(swift.change_oil())
print(swift.service_history)


