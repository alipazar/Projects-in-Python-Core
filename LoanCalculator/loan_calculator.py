
loan_principal = 1000
monthly_payment = 250
months = [1, 2, 3]
repaid_per_month = [monthly_payment, monthly_payment, monthly_payment * 2]

print(f"Loan principal: {loan_principal}")

for month, repaid in zip(months, repaid_per_month):
    print(f"Month {month}: repaid {repaid}")

print("The loan has been repaid!")
