#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:50:44 2018

@author: jamesbellagio
"""

balance = 999999
annualInterestRate = 0.18
months = 12



top = (balance*(1+annualInterestRate)**12)/12
bot = balance/12

def interest_mo(annualInterestRate):
    """ function to convert Annual percentage rate to monthly interest
    
    parameter: interest as a decimal
    
    return: interest rate for one month"""
    return annualInterestRate/months

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

#print('balance = '+str(balance))
#print('annualInterestRate = '+str(annualInterestRate))
#print('monthlyPaymentRate = '+str(monthlyPaymentRate))

#def year_ofpaying(guess, inscopebalance):
#    for i in range(12):
#        pay = mon_unpaid_bal(inscopebalance, guess)
#
#        newbalance = unpaid_w_interest(pay, monInterest)
#
#        inscopebalance = newbalance
#        print(inscopebalance)
    
# print("Remaining balance: " + format(balance, '.2f'))
def year_paidoff(initbalance,newguess):

    lastbalance = initbalance
    for i in range(12):
        pay = mon_unpaid_bal(lastbalance, newguess)
    
        newbalance = unpaid_w_interest(pay, monInterest)
        lastbalance = newbalance
    
    return newbalance
       
    
#print('Lowest Payment: ' +str(guess))


guess = (top + bot)/2

result = year_paidoff(balance,guess)
while (abs(result) >= 0.01):
    if result < 0:
        top = guess
    elif result > 0.01:
        bot = guess
    else:
        break
    guess = (top + bot)/2
    result = year_paidoff(balance,guess)
print('Lowest Payment: ' +format(guess,'.2f'))


    

#while (unpaid > 0):
#    lastbalance = balance
#    guess +=10
#    print('orig balance is ' +str(balance))
#    for i in range(12):
#        pay = mon_unpaid_bal(lastbalance, guess)
#        print('pay is ' +str(pay))
#    
#        newbalance = unpaid_w_interest(pay, monInterest)
#        lastbalance = newbalance
#        print ('newbalance is ' +str(newbalance))
#    
#        unpaid = newbalance
#        print(guess)
#       
#    
#print('Lowest Payment: ' +str(guess))
   





