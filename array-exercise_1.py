# Let us say your expense every month are listed below:
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

# Create a list to store these monthly expenses and using that find out,

monthly_expense: list[int] = [2200, 2350, 2600, 2130, 2190]

# In Feb, how many dollars you spent extra compare to January?

exta_dollars: int = monthly_expense[1] - monthly_expense[0]

# Find out your total expense in first quarter (first three months) of the year.

first_quarter: int = monthly_expense[0] + monthly_expense[1] + monthly_expense[2]

# Find out if you spent exactly 2000 dollars in any month

exactly_2000: bool = False

for money in monthly_expense:
    if money == 2000:
        exactly_2000 = True
        print("You spent exactly 2000")

# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

june_expense: int = 1980

monthly_expense.append(june_expense)

# You returned an item that you bought in a month of April and got a refund of 200$. 
# Make a correction to your monthly expense list based on this

refund_for_april: int = 200

monthly_expense[3] = monthly_expense[3] - refund_for_april

print(monthly_expense)