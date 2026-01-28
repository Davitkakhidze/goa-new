#მომხმარებელს შემოატანინეთ ქულა 0-დან 100-მდე თუ ქულა არის 100 დაპრინტეთ A+ თუ ქულა არის 80-99 დაპრინტეთ A თუ არის 60-79 დაპრინტეთ B თუ არის 50-59 დაპრინტეთ C. თუ არის 40-49 დაპრინტეთ D და 40-ზე დაბლა დაპრინტეთ F.
sando_biwi_var=int(input("what did you get"))
if sando_biwi_var==100:
    print("a gorup")
elif sando_biwi_var>=80 and sando_biwi_var<=99:
    print("b group")
elif sando_biwi_var>=40 and sando_biwi_var<=70:
    print("c group")
else: 
    print("d group")