print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you like to give? (%) "))
tip_amount = (tip_percentage / 100) * total_bill
num_people = int(input("How many people to split the bill? "))
amount_per_person = round((total_bill + tip_amount) / num_people, 2)
print(f"Each person should pay: ${amount_per_person:.2f}")