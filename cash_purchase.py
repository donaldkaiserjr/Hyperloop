from welcome_window import welcome_screen
from dtla19 import dtla19_routes
from main_exit_screen import exit_screen
from datetime import datetime
import time


#welcome_screen()

def insert_cash():
    print("Please insert your cash now. Bills you can use are $1, $5, $10, $20 only.")
    time.sleep(3)
    print("Your ticket and change are being processed...")
    time.sleep(4)
    print("processing change...")
    time.sleep(3)
    print("printing ticket....")
    time.sleep(2)
    print("........")
    time.sleep(1)
    print("Please remember to take your TICKET and CHANGE.")
        

def route_select():
    'allows user to select from dtla-19 routes'
    print("Welcome to Pay By Cash\n")
    print("Here are the prices for the routes that leave from Downtown Los Angeles station DTLA-19")
    print('\n'.join("[{}: ${}]".format(k, v) for k, v in dtla19_routes.route_1.items()))
    print('\n'.join("[{}: ${}]".format(k, v) for k, v in dtla19_routes.route_2.items()))
    print('\n'.join("[{}: ${}]".format(k, v) for k, v in dtla19_routes.route_3.items()))
    while True:
        notes = []
        entry = input("\nPlease choose a destination.\n[PRESS #290 for DTLA TO SAN FRANCISCO-SF509]\n[PRESS #387 for DTLA to Portland Oregan PRT691]\n[PRESS #498 for DTLA to Manhattan NY Grand Central Terminal]\n[PRESS #0 to EXIT] ")
        if not all(i.isdigit() for i in entry):
            notes.append("Please make sure your entry consists of numbers only.")
        if str(entry)!='#290' or str(entry)!='#387' or str(entry)!= '#498' or str(entry)!= '#0':
            notes.append("The selections to choose are: [PRESS #290 for DTLA TO SAN FRANCISCO-SF509]\n[PRESS #387 for DTLA to Portland Oregan PRT691]\n[PRESS #498 for DTLA to Manhattan NY Grand Central Terminal]\n[PRESS #0 to EXIT]")
        if len(str(entry)) < 4:
            notes.append("Your entry must start with the '#' and end with at least two numbers.")
        if len(str(entry)) > 4:
            notes.append("Please try again.")
        if len(notes) == 0:
            return insert_cash()
            break
        if str(entry) == '#290':
            print('\n'.join("\nYou have selected {}: ${}".format(k, v) for k, v in dtla19_routes.route_1.items()))
            time.sleep(2)
            return insert_cash()
        if entry == '#387':
            print('\n'.join("\nYou have selected {}: ${}".format(k, v) for k, v in dtla19_routes.route_2.items()))
            time.sleep(2)
            return insert_cash()
        if entry == '#498':
            print('\n'.join("\nYou have selected {}: ${}".format(k, v) for k, v in dtla19_routes.route_3.items()))
            time.sleep(2)
            return insert_cash()
        if entry == '#0':
            return exit_screen()
        if len(notes) == 4:
            return exit_screen()
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)


def cash_ticket():
    #This script is for riders who prefer to buy a ticket using cash
    while True:
        notes = []
        entry = input("To purchase a Hyperloop ticket with cash, please press #25.\n[#25 -CASH PURCHASE] [#99 -NEW LOOP CARD] [#0 -EXIT] ")
        if not all(i.isdigit() for i in entry):
            notes.append("Please make sure your entry consists of numbers only.")
        if str(entry)!='#25' or str(entry)!='#99' or str(entry)!= '#0':
            notes.append("The selections to choose are: [#25 Purchase a ticket with cash]  [#99 Get a new Loop Card]  [#0 EXIT]")
        if len(str(entry)) < 3:
            notes.append("Your entry must start with the '#' and end with at least two numbers.")
        if len(str(entry)) > 3:
            notes.append("Please try again.")
        if str(entry) == '#25':
            return route_select()
        if len(notes) == 0:
            return route_select()
            break
        if entry == '#0':
            return exit_screen()
        if len(notes) == 4:
            return exit_screen()
        if entry == '#99':
            from loop_card import new_card
            return new_card()
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)

cash_ticket()

