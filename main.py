print("welcome to the tip calcculator!")

bill = float(input("how much was the bill? "))
tip = float(input("how much tip would you like to give? 10,12 or 15? "))
people = int(input("how many people to split the bill? "))

total_amount =  (tip /100) * bill + bill
amount_per_person = total_amount / people

print(f"Each person should pay {amount_per_person :.2f} ")

