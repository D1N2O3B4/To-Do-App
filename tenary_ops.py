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

star = "*"
count = 10

"""Half Diamond"""
while len(star) < count:
    print(star)
    star += "*"
while len(star)> 0:
    print(star)
    star = star[:-1]

"""Full Diamond"""

while len(star) < 10:
    a = 10
    print(f"{star:^{a}}")
    star += "**"
star = star[:-1][:-1]
while len(star) > 0:
    print(f"{star:^{a}}")
    star =  star[:-1][:-1]

name = "Myelin"
print(list(enumerate(name)))

if { 'a': 34 }:
    print('The condition evaluted to True')
else:
    print('The condition evaluted to False')

print("Ok" if True else False)
