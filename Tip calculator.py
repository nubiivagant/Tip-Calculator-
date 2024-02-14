#Tip calculator project
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to Tip Calculator!")
#first we take input from the user
amount = float(input("What is the amount of total bill? $"))
tip = int(input("How much would you like to tip(in percentage)?"))
split = int(input("In how many people would you like to split the bill in?"))

#formulise the total bill adding the tip
tip_percent = tip / 100
tip_amount = amount * tip_percent
bill = amount + tip_amount
split_perperson = bill / split
final_amount = (round(split_perperson, 2))

#printing the amount using f string
print(f"Each person should pay: ${final_amount}")
