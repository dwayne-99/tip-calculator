print("Tip Calculator")
bill = float(input("What is your total bill? $"))
tip = float(input("What % would you like to tip? 10, 12, or 15? %"))
people_dining = int(input("How many people will split the bill? "))
# takes the inputs bill, tip, people_dining and saves each input in a corresponding variable

bill_with_tip = tip / 100 * bill + bill
# calculates the bill with tip included

bill_per_person = bill_with_tip / people_dining
# calculates the total bill per person dining

final_amount = "{:.2f}".format(bill_per_person)
# presents output of bill_per_person rounded/formatted to two decimal places

print(f"Each person should pay: ${final_amount}")
# prints final amount after given text
