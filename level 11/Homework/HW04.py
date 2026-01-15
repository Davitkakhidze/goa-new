#მოსწავლეს შეეკითხეთ მის მიერ მიღებული ქულა,თუ ქულა უდრის 100-ს მაშინ გამოუტანეთ "A Group),თუ იქნება 80-დან 99-მდე მაშინ გამოიტანეთ "B Group",თუ იქნება 40-დან 70-მდე მაშინ "C Group",დანარჩენ შემთხვევაში კი "D Group"
sando_biwi_var=int(input("what did you get"))
if sando_biwi_var==100:
    print("a gorup")
elif sando_biwi_var>=80 and sando_biwi_var<=99:
    print("b group")
elif sando_biwi_var>=40 and sando_biwi_var<=70:
    print("c group")
else: 
    print("d group")
