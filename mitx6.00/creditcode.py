##
##  Title: Credit statement
##  Author: James Bellagio
##  Description: Calculation of Credit Statement assignment for edx mit 6.00 week 2
##  
##
##
##
##
##


# def balance_unpaid(balance, payment):
#     """ function of remaining balance after payment
#     parameter: balance = initial balance
#     parameter: payment = payment
#     return: balance leftover after payment (can be negative)"""

#     return balance - payment

# def bal_w_interest(unpaid_balance, mo_interest):
#     """ function of balance after interest is applied
#     parameter: unpaid_balance = balance left after last payment (can be negative)
#     parameter: mo_interest = monthly percentage rate as a decimal
#     return: new balance after adding interest accrued (will not accrue interest if negative)"""
#     if (unpaid_balance < 0):
#         return 0
#     else: 
#         return unpaid_balance + (mo_interest * unpaid_balance)

# monthlyPaymentRate

# annualInterestRate

# balance

def interest_mo(annualInterestRate):
    """ function to convert Annual percentage rate to monthly interest
    parameter: interest as a decimal
    return: interest rate for one month"""
    return interest/12.0

def minimo_payment(minim_rate, last_balance):
    """ function to determine minimum monthly payment
    parameter: minim_rate = decimal value of payment rate. equivalent to percentage balance paid
    parameter: last_balance = balance after last payment
    return: minimum amount to pay (should never go negative; if last_balance is negative
            return zero"""
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

print('balance = '+str(balance))
print('annualInterestRate = '+str(annualInterestRate))
print('monthlyPaymentRate = '+str(monthlyPaymentRate))


for i in range(12):
    pay = minimo_payment(monthlyPaymentRate, balance)
    print(pay)

    newbalance = unpaid_w_interest(mon_unpaid_bal(balance, pay), monInterest)
    print(newbalance)

    balance = newbalance
    

