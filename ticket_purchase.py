from welcome_window import welcome_screen
from dtla19 import dtla19_routes
from main_exit_screen import exit_screen
from datetime import datetime
import time


def get_routeinfo():
    import dtla19    
    print('\n'.join("{}: ${}".format(k, v) for k, v in dtla19.dtla19_routes.route_information.items()))
    import main_exit_screen
    return exit_screen()

def processing(pause,text):
    #On-screen prompt displays info to passenger. Info may need time to process. Therefore, script sleeps for n seconds. 
    print(text)
    time.sleep(pause)
    
def lc_pay(amount,route):
    #Hyperloop card final screen function confirms Loop Card was charged for the ticket price and then prints ticket for rider.
    processing(0,"Please insert your Loop Card now.")
    processing(3,"...Processing")
    processing(2,"\nYour Loop Card was charged in the amount of ${} for route {}".format(amount,route))
    processing(2,"...Processing")
    processing(3,"Your ticket and change are being processed...")
    processing(1,"printing ticket....")

    line1 = datetime.now().strftime("VALID:\n%A %B %d, %Y\n\n")
    line2 = "\nDEPART:\nDowntown Los Angeles DTLA-19\n\n"
    line3 = "\nROUTE:\n"+str(route)+"\n\n"
    line4 = "\nPRICE:\n$"+str(amount)+"\n\n"
    line5 = datetime.now().strftime("\nPRINTED:\n%A %B %d, %Y\n")
    
    with open(f"{route}.txt","w") as f:
                        f.writelines([line1, line2, line3, line4, line5])
                        f.close()
    return exit_screen()

def insert_cash():
    #Final screen for passengers who bought ticket with cash.
    processing(3,"Please insert your cash now. Bills you can use are $1, $5, $10, $20 only.")
    processing(3,"Cash accepted...")
    processing(0,"printing ticket....")
    processing(1,"...Processing")
    processing(0,"Please remember to take your TICKET and CHANGE.")
    return exit_screen()
    ###########PRINT THIS TICKET###############

def route_format(text):
    print('\n'.join("[{}: ${}]".format(k, v) for k, v in text.items()))


def route_buttons():
    return "\nPlease press the corresponding code number to choose a destination:\n[PRESS 290 for DTLA TO SAN FRANCISCO-SF509]     [PRESS 387 for DTLA to Portland Oregon PRT691]\n[PRESS 498 for DTLA to Manhattan NY Grand Central Terminal]\n[PRESS 0 to EXIT]"

    
def route_select():
    'allows user to select from dtla-19 routes'
    processing(0,"Here are the prices for the routes that leave from Downtown Los Angeles station DTLA-19")
    route_format(dtla19_routes.route_1)
    route_format(dtla19_routes.route_2)
    route_format(dtla19_routes.route_3)
    processing(1,"...")
    processing(1,".....")
    processing(.5,"......")

    while True:
        notes = []
        #entry = input("\nPlease choose a destination.\n[PRESS 290 for DTLA TO SAN FRANCISCO-SF509]     [PRESS 387 for DTLA to Portland Oregon PRT691]\n[PRESS 498 for DTLA to Manhattan NY Grand Central Terminal]\n[PRESS 0 to EXIT]")
        entry = input(route_buttons())

        if not all(i.isdigit() for i in entry):
            notes.append("Please make sure your entry consists of numbers only.")
        
        if str(entry)!='290' or str(entry)!='387' or str(entry)!= '498' or str(entry)!= '0':
            notes.append(route_buttons())
        
        if len(str(entry)) < 3:
            notes.append("Your entry must be at least 3 characters or press 0 to exit.")
        
        if len(str(entry)) > 3:
            notes.append("Please try again.")
        
        if len(notes) == 0:
            return insert_cash()
            break

        if str(entry) == '290':
            print('\n'.join("\nYou have selected {}: ${}".format(k, v) for k, v in dtla19_routes.route_1.items()))
            time.sleep(1)
            payment = input('PRESS 25 to use cash now or PRESS 2 to charge your Loop Card.')
            
            if payment == '25':
                return insert_cash()
            
            if payment == '2':
                for k, v in dtla19_routes.route_1.items():
                    return lc_pay(v,k)
        
        if entry == '387':
            print('\n'.join("\nYou have selected {}: ${}".format(k, v) for k, v in dtla19_routes.route_2.items()))
            time.sleep(1)
            payment = input('PRESS 25 to use cash now or PRESS 2 to charge your Loop Card.')
            
            if payment == '25':
                return insert_cash()
            
            if payment == '2':
                for k, v in dtla19_routes.route_2.items():
                    return lc_pay(v,k)
        
        if entry == '498':
            print('\n'.join("\nYou have selected {}: ${}".format(k, v) for k, v in dtla19_routes.route_3.items()))
            time.sleep(1)
            payment = input('PRESS 25 to use cash now or PRESS 2 to charge your Loop Card.')
            
            if payment == '25':
                return insert_cash()
            
            if payment == '2':
                for k, v in dtla19_routes.route_3.items():
                    return lc_pay(v,k)
        
        if entry == '0':
            return exit_screen()

        
        if len(notes) == 4:
            return exit_screen()
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)


def cash_ticket():
    #This script is for riders who prefer to buy a ticket using cash. 
    #When passenger selects cash option, they get sent to the route select option.
    while True:
        notes = []
        entry = input("Please choose from the following options:\n\n[PRESS 25 to buy ticket using cash]  [PRESS 99 to get a new Loop Card]  [PRESS 2 to use your existing Loop Card]  \n[PRESS 0 to EXIT]")
        
        if not all(i.isdigit() for i in entry):
            notes.append("Please make sure your entry consists of numbers only.")
        
        if str(entry)!='25' or str(entry)!='99' or str(entry)!= '0':
            notes.append("The selections to choose are: [PRESS 25 to purchase a ticket with cash]  [PRESS 99 to get a new Loop Card]  [PRESS 0 to EXIT]")
        
        if len(str(entry)) < 3:
            notes.append("Your entry must be 3 characters or press 0 to exit.")
        
        if len(str(entry)) > 3:
            notes.append("Please try again.")

        if str(entry) == '25':
            return route_select()
        
        if str(entry) == '2':
            return route_select()
        
        if len(notes) == 0:
            return route_select()
            break
        
        if entry == '0':
            return exit_screen()
        
        if len(notes) == 4:
            return exit_screen()
        
        if entry == '99':
            from loop_card import new_card
            return new_card()
        
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)

#cash_ticket()

