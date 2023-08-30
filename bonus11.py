def get_average():
    with open("fip.txt","r") as f:
        lisp = f.readlines()
        print(lisp)
    value = lisp[1:]
    value = [float(i) for i in value]
    average_local = sum(value)/len(value)
    return average_local

average = get_average()
print(average)