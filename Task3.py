total = input('Enter the deposit amount: ')
period = input('Enter the deposit term (in years): ')
rate = input('Enter the annual interest rate (in %): ')

try:
    total = float(total) 
    period = int(period)
    rate = float(rate)
    S = total * ((1 + rate / 100) ** period)  
    print(f"Your total will be: {S:.2f}")
except ValueError:
    print('Please enter valid numeric values for the deposit amount, term, and interest rate.')