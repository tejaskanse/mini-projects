print("welcome to tip calculator!!")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, 15? "))
people = int(input("how many people to split the bill? "))
bill_with_tip = bill * (1 + tip / 100)
print("final bill to be paid " + str(bill_with_tip))
per_person = bill_with_tip / people
print("per person need to contribute " + str(per_person))