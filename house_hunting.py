total_cost = float(input("What is the cost of your dream home?"))
annual_salary = float(input("What is your annual salary?"))
portion_saved = float(input("What percent of your paycheck would you like to save, as a decimal?"))
annual_return = float(input("Enter the expected annual rate of return"))
down_payment = float(input("Enter the percent of your home's cost to save as a down payment"))
#variables for calculating savings from salary
r = annual_return/12
portion_down_payment = down_payment * total_cost
#current savings has to retain it's former value plus add the interest gained from that value AND add the new savings from the % of paycheck
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved
current_savings = 0
interest_earned = current_savings * r
#add together the amount saved and the amount earned from interest for monthly savings total

#print(current_savings)

#the ultimate goal is to figure out how many months have to pass before current_savings = portion_down_payment
months = 0


# while current_savings < portion_down_payment:
#     months += 1
#     current_savings = current_savings + (current_savings * r) + monthly_savings
#     # current_savings += monthly_savings

# print(months)

def house_hunting(annual_return=.004, down_payment=0.25):
    while current_savings < portion_down_payment:
        months += 1
        current_savings = current_savings + (current_savings * r) + monthly_savings
    # current_savings += monthly_savings

    print(months)

