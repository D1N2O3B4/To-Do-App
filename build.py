class Car:
    def __init__(self,brand,version,year,c_speed,hp,petrol_cap):
        self.brand = brand
        self.version = version
        self.year = year
        self.hp = hp
        self.speed = c_speed
        self.petrol_cap = petrol_cap
    
    def drive(self):
        while (self.petrol_cap > 0):
            if (self.speed != self.hp):
                self.speed += 1
            else:
                print("Limit reached")
            self.petrol_cap -= 20
            return f"Vroom speed {self.speed}"



mycar = Car("Ferrari","Nuelo",2001,123,700,1000)

print(Car.drive(mycar))