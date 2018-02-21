#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 08:39:57 2018

@author: jamesbellagio
"""

topBound = 100
botBound = 0
def guessNum (top,bot):
    return (top+bot)/2;

guess = int(guessNum (topBound,botBound))

answer = ''

while (answer != 'c'):
    print('Is your secret number '+ str(guess) +'?')
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if (answer == 'h'):
        topBound = guess
        guess = int(guessNum (topBound,botBound))
    elif (answer == 'l'):
        botBound = guess
        guess = int(guessNum (topBound,botBound))
    elif (answer == 'c'):
        print('Game over. Your secret number was: '+ str(guess))
        break
    else:
        print('Sorry, I did not understand your input.')