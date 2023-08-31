a = 0
try:
    print(56/a)
except ZeroDivisionError:
    print("Caught Zero Division error")
finally:
    print("I run regardless of the outcome")