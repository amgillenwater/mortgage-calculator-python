total_cost = float(input("What is the cost of your dream home?"))
annual_salary = float(input("What is your annual salary?"))
portion_saved = float(input("What percent of your paycheck would you like to save, as a decimal?"))

#variables for calculating savings from salary
r = 0.04/12
portion_down_payment = 0.25 * total_cost
#current savings has to retain it's former value plus add the interest gained from that value AND add the new savings from the % of paycheck
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved
current_savings = 0
interest_earned = current_savings * r
total_month_savings = monthly_savings + interest_earned
#add together the amount saved and the amount earned from interest for monthly savings total

#print(current_savings)

#the ultimate goal is to figure out how many months have to pass before current_savings = portion_down_payment
months = 0


while current_savings < portion_down_payment:
    months += 1
    current_savings = current_savings + current_savings * r
    current_savings += monthly_savings

print(months)

