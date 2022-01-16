
print("#myscript.ps1")
print("my name is Raz")
print("this is my most common used script")

with open('ops.txt') as f:
    if 'Dave' in f.read():
        print("the String Dave existing in the file ops.txt")
    else:
        print("the String Dave not existing in the file ops.txt")




