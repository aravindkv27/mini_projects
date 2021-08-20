print("Python Pizza")
pizza=input("Enter the size of the pizza..\nSmall S\nMedium M\nLarge L\n")

print("Can We add Pepperoni :")
pepperoni=input("Enter Y for Yes And N for No : ")
extra_cheese = input("Do you want extra cheese Y or N : ")


if pizza == "S":
    pay=15
    print(f"Small Pizza : {pay}")
    if pepperoni=="Y":
        pay+=2

elif pizza == "M":
    pay=20
    print(f"Medium Pizza : {pay}")
    if pepperoni=="Y":
        pay+=3

elif pizza == "L":
    pay=25
    print(f"Large Pizza : {pay}")
    if pepperoni=="Y":
        pay+=3
if extra_cheese=="Y":
    pay+=1
    print(f"Your Final Bill is : {pay}")
    

else:
    print("Enter the Correct Option.")
