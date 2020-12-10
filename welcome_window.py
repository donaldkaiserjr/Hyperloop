from datetime import datetime
import dtla19
import time

def welcome_screen():
    print('\nWelcome to Hyperloop @ Union Station, Downtown Los Angeles DTLA-19.')
    print(datetime.now().strftime("Today is %A, %B %d, %Y\n"))
    time.sleep(1)


#welcome_screen()