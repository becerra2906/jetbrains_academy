### By: Alejandro Becerra 
#done as part of Jet Brains Academy Python learning Path
#serves to calculate the number of months required to pay for a 
#flight with miles generated with customer credit card purchases.

#print welcome message

print("""Hi! Welcome to your credit card miles calculator. 
This program will help you understand how many months do you need to spend at your current
rate to get enough miles to travel to several destinations!""")
 
monthly_expenditure = abs(float(input("How much do you spend with your credit card? ")))

#definition of point rate per dollar spent

point_earning_rate = abs(float(input("How many points per dollar do you get with your card? ")))

#distances to different world renowned cities

new_york_distance = abs(int(input("How far away in miles are you from New York? ")))

paris_distance = abs(int(input("How far away in miles are you from Paris? ")))

mumbai_distance = abs(int(input("How far away in miles are you from Mumbai? ")))

# miles earnt per month

miles_per_month = (monthly_expenditure * point_earning_rate)

# calculation of months needed to get round trip
# to different destinations using miles

months_ny = int((new_york_distance * 2) / miles_per_month)

months_paris =  int((paris_distance * 2) / miles_per_month)

months_mumbai = int((mumbai_distance* 2) / miles_per_month)

#print function for resulting months required to get tickets

message_part_1 = 'It would take you '
message_part_2 = ' months to get a round trip to '
new_york_str = 'New York. '
paris_str = 'Paris. '
mumbai_str = 'Mumbai. '

ny = (message_part_1 + str(months_ny) + message_part_2 + new_york_str)
paris = (message_part_1 + str(months_paris) + message_part_2 + paris_str)
mumbai = (message_part_1 + str(months_mumbai) +  message_part_2 + mumbai_str)

print(ny)
print(paris)
print(mumbai)
# print farewell message

print("Thank you for using our program! Fly far away!")
