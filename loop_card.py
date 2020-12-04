from datetime import datetime
import re 

def welcome_screen():
    print('Welcome to the Loop Card payment system for Hyperloop.')
    print('This system allows you to add money to your card and charges your card for riding the Hyperloop.')
    print(datetime.now().strftime("\nToday is %A, %B %d, %Y"))
    

welcome_screen()


def new_card():
    while True:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email_notes = []
        psw_notes = []

        user_email = input("Enter your email address: ")
        if not(re.search(regex,user_email)):  
            print("Invalid Email")
            email_notes.append("Your emails do not match. Please try again.")  
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
            return new_pin()
        if pin_number == '#99':
            return new_card()
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)

pin_input()




automation = input('Press The Enter Key')
automation = ['processing...', '10...', '20...', '30...', '40...', '50...', '60...', '70..', '80..', '90.', '100']
for a in automation:
    print(a)
print('Automation Successful')

print('How much would you like to recharge on your card?, You are adviced to recharge $30 dollars')

Recharge_Amount = input()
transaction = ['processing...', '10...', '20...', '30...', '40...', '50...', '60...', '70..', '80..', '90.', '100']
for t in transaction:
    print(t)
print('Recharge Successful')

print('Lists of stations')

stations = ['5th', 'Pelham Parkway', 'Bronx', 'Guns Hill']
for s in stations:
    print (s)

stations_select = input()

print('Lists of zones')
zones = ['zone 1', 'zone 2', 'zone 3']
for z in zones:
    print (z)

print('Kindly move on through the barrier, swipe your card and select your fare')

print('Below are the Fares for each journey, ' + ' Select a, b, or c.')
print('              Journey                 |       Fare    ')
print('(a)  Anywhere in Zone 1               |       $2.50   ')
print('(b)  Any one zone outside Zone 1      |       $2.00   ')
print('(c)  Any two zones including Zone 1   |       $3.00   ')
print('(d)  Any two zones excluding Zone 1   |       $2.25   ')
print('(e)  Any three zones                  |       $3.20   ')
print('(f)  All bus journey                  |       $1.80   ')

balance = 30
journey = input()
if journey == 'a':
    print('Balance:')
    print(30 - 2.50)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'b':
    print('Balance:')
    print(30 - 2.00)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'c':
    print('Balance:')
    print(30 - 3.00)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'd':
    print('Balance:')
    print(30 - 2.25)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'e':
    print('Balance:')
    print(30 - 3.20)
    print('Your fare has been deducted, please proceed to your train')
elif journey == 'f':
    print('Balance:')
    print(30 - 1.80)
    print('Your fare has been deducted, please proceed to your train')
else:
    print('You have not selected any fare')
    exit()





"""
bankaccount = input()
if len(bankaccount) != 10:
    print('Sorry, Incorrect Bank Account, try again')
    bankaccount = input()
if len(bankaccount) != 10:
    print('Place your thumb on the sensor for automated derivation of bank details')
    
"""