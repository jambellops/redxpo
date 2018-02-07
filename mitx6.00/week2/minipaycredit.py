# Paste your code into this box
def interest_mo(annualInterestRate):
    """ function to convert Annual percentage rate to monthly interest
    
    parameter: interest as a decimal
    
    return: interest rate for one month"""
    return annualInterestRate/12.0

def minimo_payment(minim_rate, last_balance):
    """ function to determine minimum monthly payment
    
    parameter: minim_rate = decimal value of payment rate. equivalent to 
    percentage balance paid
    
    parameter: last_balance = balance after last payment
    
    return: minimum amount to pay (should never go negative; if last_balance is
    negative return zero"""
    if (last_balance < 0):
        return 0
    else:
        return minim_rate * last_balance

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


for i in range(12):
    pay = minimo_payment(monthlyPaymentRate, balance)

    newbalance = unpaid_w_interest(mon_unpaid_bal(balance, pay), monInterest)

    balance = newbalance
    
print("Remaining balance: " + format(balance, '.2f'))

