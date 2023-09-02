"""FEET TO METRES CONVERTER"""
feetVal = input("Type feet followed by a \" then the inches of your height: ")


def parse():
    lisp = feetVal.split('"')
    feet = float(lisp[0])
    inches = float(lisp[1])
    return {'feet':feet,'inches':inches}

def convertToMetres(feet,inches):
    metres = feet*.3048 + inches*.0254
    return f"{int(feet)}\"{int(inches)} is {metres} in metres"
    
parsed = parse()
print(convertToMetres(parsed['feet'],parsed['inches']))