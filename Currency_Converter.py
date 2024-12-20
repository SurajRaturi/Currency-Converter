 # Currency Converting programme
for i in range(0,160):
    print("-", end = "")
    print("-", end = "")
print("\t \t \t \t \t \t \t \t **WELOCME TO CURRENCY CONVERTER PROGRAMME: **")
print()
for  j in range(0,160):
    print("-",end="")
print("\t \t \t \t \t \t \tChose the conversion of the currency from given below :")
for k in range(0,160):
    print("-",end="")
print("\t \t \t \t \t \t \t  \t \t 1.) Indian Rupee : (INR)")
print("\t \t \t \t \t \t \t  \t  2.) US Dolloar : (USD) ")
print("\t \t \t \t \t \t \t  \t  3.) Euro : (EURO)")
print("\n \n \n")
for l in range(0,160):
    print("-",end= "")
    print("-",end="")
def condition():
    while True:
        a=input("Enter the currency standard form which you want to convert : - ")
        b=input("Enter the currency standard  form in which you to convert : -  ")
        c=int(input("Enter the amount you want to do conversion : -  "  ))
        if a=="INR" and b=="USD":
            print("1 INR = 0.012 USD")
            print("\n \n")
            print(f"The amount converted is equal to :-  {c*0.012} ")   
        elif a=="USD" and b=="INR":
            print("1 USD = 85.03 INR")
            print("\n \n ")
            print(f"The amount converted is equal  to :-  {c*85.03}")
        elif a=="INR" and b=="EURO":
            print("1 INR = 0.011 EURO")
            print("\n \n")
            print(f"The amount which is converted is equal to  : -  {c*0.011}")
        elif a=="EURO" and b=="INR":
            print("1 EURO = 88.37 INR")
            print("\n \n")
            print(f"The amount which is converted is equal to : -  {c*88.37}")
        elif a=="USD" and b=="EURO":
            print("1 USD = 0.96 EURO")
            print("\n \n ")
            print(f"The amount which is converted is equal to : - {c*0.96}")
        elif a=="EURO" and b=="USD":
            print("1 EURO = 1.04")
            print("\n \n")
            print(f"The amount which is converted is equal to : -  {c*1.04}")
        print("\n \n")
        d=int(input("Press 1 for converting again . \nPress 2 for exit...."))
        if d==1:
            print()
            continue
        elif d==2:
            print()
            break
        else:
            print("Invalid input! Please enter correct .")
    
condition()

    




