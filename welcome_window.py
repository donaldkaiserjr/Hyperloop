from datetime import datetime


def welcome_screen():
    print(datetime.now().strftime("\nToday is %A, %B %d, %Y"))
    print('Welcome to the Loop Card payment system for Hyperloop.')
    print('Please Enter Your Loop Card now or press #100 to purchase a ticket using cash. ')