from datetime import datetime, timedelta
import time
import math

class TransportCheckIn:
    '''This class is to store data pertaining to ticket purchases and 
    the various stations and routes for the soon-to-be-released 
    Hyperloop train created by Elon Musk.
    '''
    vehicle = 'Public Transportation Station'
    total_trips = 0
    
    def __init__(self):
        self.checkin_info = []

    def register(self,fname,lname,handicapped=None,five_day_flex=None,date=datetime.today().strftime('%m-%d-%Y'),checkin_time=time.time()):
        self.fname = fname
        self.lname = lname
        self.date = date
        self.handicapped = handicapped
        self.five_day_flex = five_day_flex
        self.checkin_time = checkin_time
        conditions = True
        if len(str(fname)) < 2 or len(str(lname)) < 2:
            print('Names must be at least 2 characters.')
            conditions = False
        
        if conditions == True:
            print('Your ticket is ready for credit card purchase.')
            TransportCheckIn.total_trips += 1
            self.checkin_info = [fname,lname,date,checkin_time]

    def display(self):
        print(f'{self.fname} {self.lname} {self.date} {self.checkin_time}')

    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    @fullname.setter
    def fullname(self,name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname
        return '{} {}'.format(self.fname,self.lname)

    @fullname.deleter
    def fullname(self):
        print(f'{self.fname} {self.lname} deleted.')
        self.fname = None
        self.lname = None

    def __repr__(self):
        return "Passenger('{}', '{}', '{}','{}', '{}', '{}')".format(self.fname, self.lname, self.date, self.handicapped, self.five_day_flex, self.checkin_time)

    def __len__(self):
        return len(self.fullname)

    def add_route(self,route_num,home_station,destination,distance,depart_time=None,travel_time=None,price=15,**kwargs):
        conditions = True
        [conditions for key, value in kwargs.items() if value==0 or value==None] 
        for key, value in kwargs.items():
            if value > 0:
                deduction = value * price
                price = price - float(deduction)
        return f'{route_num} from {home_station} to {destination} is priced at ${round(price,2)}. Total distance: {distance}\n'
    
    def calculate_hc_price(self):
        '''handicap discount 20%'''
        answer = False
        [answer if self.handicapped == 'No'.lower() or 'NO'.lower() else not answer]
        if self.handicapped == 'Yes'.lower() or 'YES'.lower():
                discounted = price * .20
                price = price - float(discounted)
                return f'The price for handicap seating is {round(price,2)}'
                answer = True

class DTLA_Station19(TransportCheckIn):
    ''' Station located in Downtown Los Angeles,
    Union Station.'''

    vehicle = "Hyperloop"
    station = "Station DTLA-19"
    total_trips = 0
    
    
    def __init__(self,route105=None,route106=None):
        super().__init__()
        if route105 == None:
            self.route105 = []
        else:
            self.route105 = TransportCheckIn().add_route('Route105','DTLA-19','StationVG-19-LasVegas','270 miles',depart_time='3:45pm',price=17)
        if route106 == None:
            self.route106 = []
        else:
            self.route106 = TransportCheckIn().add_route('Route106','DTLA-19','StationSF-19-SanFrancisco','270 miles',depart_time='7:00pm',price=25)

    
    #DTLA-->to-->Las Vegas Station-VG-19    270-Miles One-way    Time of travel -18 minutes   
    #DTLA-->to-->San Francisco   Station-SF-19 --381.9 miles'




goulash = DTLA_Station19(route105=True)
goulash.register('David','Mancea','Yes')
print(goulash.__repr__())




'''
    #DTLA-->to-->San Francisco Station SF-19 --381.9 miles
    def route208_seat_price(self,price208=17):
        return price208

    #DTLA-->to-->, Downtown Manhattan NY Station NYDM-19   --2,789.4 miles
    def route301_seat_price(self,price301=24):
        return price301
'''



if __name__ == "__main__":
   Trans_obj = TransportCheckIn()
   DTLAStat19_obj = DTLA_Station19()




Copyright-Donald Kaiser
