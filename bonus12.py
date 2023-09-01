"""FEET TO METRES CONVERTER"""
feetVal = input("Type feet followed by a \" then the inches of your height: ")

def convertToMetres(feetVal):
    lisp = feetVal.split('"')
    feet = float(lisp[0])
    inches = float(lisp[1])
    metres = feet*.3048 + inches*.0254
    return f"{lisp[0]}\"{lisp[1]} is {metres} in metres"
    
print(convertToMetres(feetVal))