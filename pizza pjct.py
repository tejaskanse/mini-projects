print("welcome to sizzler pizza..!")
bill = 0

pizaa_choice=input("1-Farm House.\n2-Peppy Paneer.\n3-Mexican Green Wave.\n4-Deluxe Veggie.\n5-Veg Extravaganza.\nwhich pizza do you want?\n ")
if pizaa_choice== '1':
    bill+=200
elif pizaa_choice=='2':
    bill+=220
elif pizaa_choice=='3':
    bill+=260
elif pizaa_choice =='4':
    bill+=240
elif pizaa_choice=='5':
    bill+=180
else:
    print("choose right choice\n")
    exit()
    
size = input("please select your size of pizza? \n S , M or L\n") 
if size.upper() == "S":
    bill += 150
elif size.upper() == "M":
    bill += 200
elif size.upper() == "L":
    bill += 250
else:
    print("choose right size")
    
add_pepperoni = input("do you want pepperoni?\n Y or N\n")
if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 20
    elif size.upper() =="M":
        bill += 30
    elif size.upper() =="L":
        bill += 40

extra_cheese = input("do you want extra cheese?\n Y or N\n")    
if extra_cheese.upper() == "Y":
    bill += 10

print("Your total bill is " + str(bill)+ ". thank you to visit us." )

