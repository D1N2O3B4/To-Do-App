date = input("Input today's date: ")
experience = input("How was your day from 1 - 10?")
description = input("Describe your day: ")+"\n"
with open(date+".txt","w") as f:
    f.writelines(experience+"\n")
    f.writelines(description)