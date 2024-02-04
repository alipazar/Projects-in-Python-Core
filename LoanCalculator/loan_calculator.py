import math


loan_principal = int(input("Enter the loan principal:\n> "))


calculation_type = input("What do you want to calculate?\n"
                        'type "m" for number of monthly payments,\n'
                        'type "p" for the monthly payment:\n> ')

if calculation_type == "m":

    monthly_payment = int(input("Enter the monthly payment:\n> "))
    months = math.ceil(loan_principal / monthly_payment)

    if months == 1:
        print("It will take 1 month to repay the loan")
    else:
        print(f"It will take {months} months to repay the loan")

elif calculation_type == "p":

    num_of_months = int(input("Enter the number of months:\n> "))
    monthly_payment = math.ceil(loan_principal / num_of_months)
    last_payment = loan_principal - (num_of_months - 1) * monthly_payment

    if last_payment == monthly_payment:
        print(f"Your monthly payment = {monthly_payment}")
    else:
        print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}.")
