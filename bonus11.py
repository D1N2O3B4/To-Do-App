def get_average():
    with open("num.txt","r") as f:
        nums = f.readlines()
    value = nums[1:]
    value = [float(i) for i in value]
    average_local = sum(value)/len(value)
    return average_local

average = get_average()
print(average)