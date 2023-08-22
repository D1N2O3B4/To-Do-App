content = ["lorem ispum","Marksis","Denifatetley"]

filenames = ["doc.txt","report.txt","presentation.txt"]

for i in range(len(content)):
    with open(filenames[i],"w") as f:
        f.writelines(content[i])
