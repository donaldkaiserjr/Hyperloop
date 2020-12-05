

def dtla19_routes():
    '''DTLA-19 @ Union Station Downtown Los Angeles'''
    
    #DTLA-19 Routes with mileage.
    routes = {"290-to-SanFran-SF509": 382.9, "387-to-PortOR-PRT691": 962.2}
    sf290_price = 9.50

    
    for value in routes:
        print(routes.get(value))



dtla19_routes()
















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
def rerun():
    for rerun in range(2):
        cc_checker()

rerun()
"""

