note1=float(input("donner la premiére note:"))
note2=float(input("donner la deuxiéme note:"))
note3=float(input("donner la troisiéme note:"))
note4=float(input("donner la 4 note:"))

moyenne=(note1 + note2 + note3)/3
print("la moyenne est:",moyenne)

if moyenne >= 10:
    print("Admis")
else:
    print("Non admis")


