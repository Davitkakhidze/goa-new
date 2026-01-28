#მომხმარებელს შემოატანინე პაროლი და თუ ის არის 8 ციფრზე ნაკლები დაპრინტე "სუსტი პაროლი" და სხვა შემთხვევაში დაპრინტე "ძლიერი პაროლი".
rr2 =input("your password")
if len(rr2)<8:
    print("susti pasword")

else:
    print("strong password")