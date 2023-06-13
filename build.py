lisp = ["Body","Ora","Mist","Beam","Lora","Mika"]

for_b = [i for i in lisp if i[0] == "B"]
print(for_b)

for_a = [j for j in lisp if j[len(j)-1] == "a"]
print(for_a)