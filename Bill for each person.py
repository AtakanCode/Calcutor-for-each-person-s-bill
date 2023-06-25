print("Welcome to tip calculator\n")
bill = float(input("What was the total bill? $"))
percentage_of_tip = int(
input("What percentage tip would you like to give? 10, 12, or 15 "))
total_bill = bill * (1 + percentage_of_tip / 100)
split = int(input("How many people to split the bill? "))
each_person = round(total_bill / split, 2)
each_person = "{:.2f}".format(each_person)
print(f"Each person should pay ${each_person}")
