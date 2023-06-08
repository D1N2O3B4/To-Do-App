from urllib.request import urlretrieve  
from urllib3 import request
import os
# x,y = 5,6
# print("x" if x > y else "y")

# a,b = 5,3

# print((b,a) [a<b])

# test = 3.0
# print(test)
# test = 21.0
# print(test)

# expo = 6.02e23
# print(expo)

# name = "David"

# print("D" in name)

# player1 = "Sam Cole"
# player2 = "J Cole"
# player3 = player1.replace("Sam","Patrick")
# print(player3)


# txt = ",,,,,rrttgg.....banana....rrr"

# x = txt.strip(",rtg")

# print(x)

# sentence = """  Hello  we are you    
# but could be mee  
#   so come here"""

# print(sentence.strip())

# player = dict(name="Melo",no = 1,position = "Point Guard")
# print(player)

# print(player.get("name"))
# print(player.get("age",None)) #This checks if age is a key if not return the message None

# lso = ["Aw"]
# lso[0] = "Mt.Human"#works if the list already has members
# print(lso)

# #Copying makes sure the orignal variable is not affected
# down = [1,23,4,12,66]

# for i in range(10):
#     print(i,end="-")#to prevent new lines from occuring

# name = "David" if False else "Stan"
# print("My name is {}".format(name))

# star = "*"
# count = 10

# """Half Diamond"""
# while len(star) < count:
#     print(star)
#     star += "*"
# while len(star)> 0:
#     print(star)
#     star = star[:-1]

# """Full Diamond"""

# while len(star) < 10:
#     a = 10
#     print(f"{star:^{a}}")
#     star += "**"
# star = star[:-1][:-1]
# while len(star) > 0:
#     print(f"{star:^{a}}")
#     star =  star[:-1][:-1]

# name = "Myelin"
# print(list(enumerate(name)))

# if { 'a': 34 }:
#     print('The condition evaluted to True')
# else:
#     print('The condition evaluted to False')

# print("Ok" if True else False)

# a = 10

# if a % 2 == 0:
#     print("Two")
# if a % 5 == 0:
#     print("Five")
# else:
#     print("Nothing")

# print(3e3)
# print(3e-3)
# print()


# def all(lisp):
#     for i in lisp:
#         print(i)

# print(all([1,2,5,6,12,33]))
# print("****")
# for i in [1,2,5,6,12,33]:
#     print(i)

# a = 12

# try:
#     c = a/3
#     print("Worked")

# except OSError:
#     print('Value ebing divided not possible')

# except Exception:
#     print("Trying to divide by zero not possible")

# except SyntaxError:
#     print("Trying to divide by zero not possible")
# else:
#     print("We work if nothing happens")
# finally:
#     print('I will always work no matter what')

# a = os.getcwdb()
# print(a.upper())
# print(a.decode())
# print(os.listdir('/Users'))
# os.makedirs("./Created",exist_ok=True) # The exist_ok = True acts as an error handler in case you call the statement and the folder already exists

# print("Create" in os.listdir("."))
# print(os.listdir("Created"))

url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'

urlretrieve(url1,"./Created/read.txt")

def listify(values):
    return values.strip().split(",")

# # r = request.get('https://api.github.com/user', auth=('user', 'pass'))
with open("./Created/read.txt","r") as file2:
    # print(file2.read())
    read_f = file2.readlines()
    print(listify(read_f[0]))