
print("#myscript.ps1")
print("my name is Raz")
print("this is my most common used script")
print("git log --oneline --decorate –graph")
print("checking if the string “Dave” exists in file “Ops.txt”")

with open('ops.txt') as f:
    if 'Dave' in f.read():
        print("the String Dave existing in the file ops.txt")
    else:
        print("the String Dave not existing in the file ops.txt")




