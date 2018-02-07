# Paste your code into this box
months = 12

guess = 0
unpaid = 1

def interest_mo(annualInterestRate):
    """ function to convert Annual percentage rate to monthly interest
    
    parameter: interest as a decimal
    
    return: interest rate for one month"""
    return annualInterestRate/12.0

def mon_unpaid_bal(last_balance, payment):
    """ function to determine upaid portion of balance
    
    paremeter: last_balance = balance after last payment
    
    parameter: payment = current payment
    
    return: unpaid balance after payment is applied"""
    return last_balance - payment
def unpaid_w_interest(unpaid, interest):
    """function to determine balance after interest is applied
   
    parameter: unpaid = balance after payment is applied
    
    parameter: interest = monthly interest as a decimal
    
    return: new balance with interest"""
    return unpaid + unpaid*interest

monInterest = interest_mo(annualInterestRate)

while (unpaid > 0):
    lastbalance = balance
    guess +=10
    for i in range(12):
        pay = mon_unpaid_bal(lastbalance, guess)
    
        newbalance = unpaid_w_interest(pay, monInterest)
        lastbalance = newbalance
    
        unpaid = newbalance
       
    
print('Lowest Payment: ' +str(guess))

