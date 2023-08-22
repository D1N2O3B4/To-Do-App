lisp = ["1.file1","2.file2","3.file3"]
lisp = [item.replace(".","-")+".txt" for item in lisp]
print(lisp)