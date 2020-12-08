from datetime import datetime
import re 
import random, os, sys
from sys import argv
from random import randrange, choice
from time import sleep
from welcome_window import welcome_screen

# Hyperloop card is for passengers who need to purchase a card at the station. Passengers who
# may not have access to Wifi connection or who do not possess a Hyperloop app can use the card. 
    
welcome_screen()

def new_card():
    while True:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email_notes = []
        psw_notes = []
        #Since passenger may not have access to a wifi at time of purchase, the Loop Card will not send a confirmation email. 
        #Passenger simply confirms their email twice for accuracy. 
        user_email = input("Enter your email address: ")
        if not(re.search(regex,user_email)):  
            print("Invalid Email")
            email_notes.append("Invalid email.")  
        if(re.search(regex,user_email)):  
            print("Valid Email")
        email_reentry = input("Please confirm your email by entering it again: ")
        if user_email != email_reentry:
            email_notes.append("Your emails do not match. Please try again.")
        if len(email_notes) == 0:
            print("Your email was created successfully!")
        else:
            print("Please check the following: ")
            for note in email_notes:
                print(note)

        if len(email_notes) == 0:
            pin_number = input("Enter a new 4-digit pin number: ")
            if not all(i.isdigit() for i in pin_number):
                psw_notes.append("Pin number must consist of numbers only.")
            if len(str(pin_number)) < 4:
                psw_notes.append("Pin number must be at least 4 characters")
            if len(str(pin_number)) > 4:
                psw_notes.append("Pin number cannot be more than 4 characters")
            if len(psw_notes) == 0:
                print("Your Pin number was entered correctly")
                with open(f"{user_email}.txt","w") as f:
                    f.write(str(user_email)+"\n")
                    f.close()
                break
            if len(psw_notes) == 4:
                print("....Your card has been returned. Please try again.")
            else:
                print("Please check the following: ")
                for note in psw_notes:
                    print(note)
        else:
            return new_card()

def new_pin():
    while True:
        notes = []
        pin_change = input("Enter your new pin number: ")
        if not all(i.isdigit() for i in pin_change):
            notes.append("Pin number must consist of numbers only.")
        if len(str(pin_change)) < 4:
            notes.append("Pin number must be at least 4 characters")
        if len(str(pin_change)) > 4:
            notes.append("Pin number cannot be more than 4 characters")
        if len(notes) == 0:
            print("Your Pin number was entered correctly")
            break
        if len(notes) == 4:
            print("....Your card has been returned. Please try again.")
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)
    
def pin_input():
    while True:
        notes = []
        pin_number = input("(press #99 to get a new card or #98 to change your pin number)\nEnter your pin number: ")
        if not all(i.isdigit() for i in pin_number):
            notes.append("Pin number must consist of numbers only.")
        if len(str(pin_number)) < 4:
            notes.append("Pin number must be at least 4 characters")
        if len(str(pin_number)) > 4:
            notes.append("Pin number cannot be more than 4 characters")
        if len(notes) == 0:
            print("Your Pin number was entered correctly")
            break
        if len(notes) == 4:
            print("....Your card has been returned. Please try again.")
        if pin_number == '#98':
            pin_validate = input("To change your pin, enter your old pin now:  ")
            if not all(i.isdigit() for i in pin_validate):
                notes.append("Pin number must consist of numbers only.")
            if len(str(pin_validate)) < 4:
                notes.append("Pin number must be at least 4 characters")
            if len(str(pin_validate)) > 4:
                notes.append("Pin number cannot be more than 4 characters")
            if len(notes) == 0:
                print("Your Pin number was entered correctly")
                break
            if len(notes) == 4:
                print("....Your card has been returned. Please try again.")
            return new_pin()
        if pin_number == '#99':
            return new_card()
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)

pin_input()

def cc_checker():
    #The cc_checker was created c/o Shankhesh-16. Screenshot png files are included.
    #C/O Shankhesh-16: https://github.com/bl4ckbo7/PyCreditCardValidator/blob/master/Credit%20Card%20Validator.py
    #This is free and unencumbered software released into the public domain. Anyone is free to copy, modify, use this software, either in source code form or as a compiled binary
    #In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit 
    #of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.
    #THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    #IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    #For more information, please refer to <https://unlicense.org>
    
    cc = input('Add money to your Loop Card now by entering your 16-digit debit card number: ')
    credit_card_number = []
    for digit in cc:
        credit_card_number.append(digit)

    if len(credit_card_number) > 0:

        after_doubling_number = []
        for index in range(len(credit_card_number)):
            if index % 2 == 0:
                after_doubling_number.append(int(credit_card_number[index]) * 2)
            else:
                after_doubling_number.append(int(credit_card_number[index]))

        #print(after_doubling_number)

        after_subtracting_list = []
        for index1 in range(len(after_doubling_number)):
            if index1 % 2 == 0 and after_doubling_number[index1] > 9:
                nine_subtraction_value = after_doubling_number[index1] - 9
                after_subtracting_list.append(nine_subtraction_value)
            else:
                after_subtracting_list.append(after_doubling_number[index1])

        #print(after_subtracting_list)

        list_to_number = ""
        for index2 in range(len(credit_card_number)):
            list_to_number += str(credit_card_number[index2])

        sum_of_final_list = sum(after_subtracting_list)

        if sum_of_final_list % 10 == 0:
            print("VALID!!")
            print(list_to_number)
        else:
            print("INVALID")
            print(list_to_number)

    else:
        print('Please check the length of the number.')

cc_checker()


def loopcard_boost():
    '''Passenger deposits funds to loop card (loop boost)'''
    while True:
        notes = []
        balance = []
        boost_values = ['5','10','20','40','60','80','100']
        print('\nBOOST AMOUNTS: {}'.format(boost_values))
        boost_amount = input('From the list above, enter an amount to add to your Loop Card: ')
        if not all(i.isdigit() for i in boost_amount):
                notes.append("Entry must consist of numbers only.")
        
        if boost_amount not in boost_values:
            notes.append('Please enter a value from the list only: '.format(boost_values))

        if len(notes) == 0:
            balance.append(boost_amount)
            print("\nSuccess!! Your Loop Card is now boosted with an extra ${}.".format(boost_amount))
            print("CURRENT BALANCE: ${}".format(" ".join(balance)))
            break
            
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)

loopcard_boost()


def lc_exit_screen():
    print(datetime.now().strftime("\n%A, %B %d, %Y"))
    print('Thank you for using the Loop Card payment system for Hyperloop.')
    print('Please take your card now.\n')
    while True:
        notes = []
        pin_number = input("(press #98 to return your card or #92 to add more money to your card: ")
        if not all(i.isdigit() for i in pin_number):
            notes.append("Selection must consist of numbers only.")
        if len(notes) == 4:
            print("....Your card has been returned. Please try again.")
        if pin_number == '92':
            return loopcard_boost()
        if pin_number == '#98':
            print("...Please remember to take your card. Thanks for using Hyperloop!")
        if len(notes) == 0:
            print("Thanks for using the Hyperloop system. See you next time!")
            break
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)

lc_exit_screen()


