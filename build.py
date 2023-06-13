for i in range(2,10):
    for j in range(2,i):
        if i%j == 0:
            print("Not prime")
            break
    else:
        print("Prime")
