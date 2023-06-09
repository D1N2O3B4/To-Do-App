import pandas as pd
# class Car:
#     def __init__(self,brand,version,year,hp,petrol_cap):
#         self.brand = brand
#         self.version = version
#         self.year = year
#         self.hp = hp
#         self.speed = 0
#         self.petrol_cap = petrol_cap
    
#     def drive(self,distance):
#         while (self.speed < self.hp):
#             self.speed += 1
#             print(f"increasing speed {self.speed} mph")
        
#         # while distance > 0:




# mycar = Car("Ferrari","Nuelo",2001,700,1000)

# print(Car.drive(mycar,30))


def split_headers(object):
    return object.strip().split(",")

def split_values(object):
    new_values = []
    for i in object.strip().split(","):
        try:
            new_values.append(i)
        except ValueError:
            new_values.append(0.0)
    return new_values

def dictyfy(val,head):
    return dict(zip(head,val))

final = []
with open("./Created/read.txt","r") as r:
    p = r.readlines()
headers = p[0]
arranged_headers = split_headers(headers)
values = p[1:]

for i in values:
    arranged_values = split_values(i)
    end = dictyfy(arranged_values,arranged_headers)
    final.append(end)
print(final)

# push = pd.read_csv("./Created/read.txt")

# def write_csv(items, path):
#     # Open the file in write mode
#     with open(path, 'w') as f:
#         # Return if there's nothing to write
#         if len(items) == 0:
#             return
        
#         # Write the headers in the first line
#         headers = list(items[0].keys())
#         f.write(','.join(headers) + '\n')
        
#         # Write one item per line
#         for item in items:
#             values = []
#             for header in headers:
#                 values.append(str(item.get(header, "")))
#             f.write(','.join(values) + "\n")

# write_csv(push,"emi.csv")
