print("Tip Calculator")

tip = float(input("What % would you like to tip? 10, 12, or 15? %"))
people_dining = int(input("How many people will split the bill? "))

# Calculates the bill with tip included
bill_with_tip = tip / 100 * bill + bill

# Calculates the total bill per person dining
bill_per_person = bill_with_tip / people_dining

# Presents output of bill_per_person rounded/formatted to two decimal places
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
