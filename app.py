from datetime import datetime, timedelta

class TransportCheckIn:
    '''This class is intended to be a passenger walk-up purchase app for passengers of the  
    the future Hyperloop system. Since there is a chance that Hyperloop could fail to launch or major
    changes could cause the technology to evolve into something unforeseeable, the Hyperloop class
    will inherit from the parent class: TransportCheckIn
    '''
    total_trips = 0
    #TRAVEL INFO
    #Dates of trips
    #time of trips
    # One-Way
    # Round-Trip
    # City From = current Location
    # City to
    # Cost (def nonstop,   def one-way)
    #  Time of trip

    #class information : Price Set (different times)
    # cities list abbreviated names
    '''
    city_list = ['Las Vegas', 'Los Angeles', 'New York', 'San Francisco']
    Vegas_LA = "las vegas to los angeles"  #270 miles
    Vegas_NY = "Vegas to New York"  #2,521.8 miles
    Vegas_SF = "Vegas to SF"  #569.0 miles

    LA_NY = "LA to New York" #2,789.4 miles
    LA_SF = "LA to SF"  #381.9 miles

    NY_SF = "NY to SF" #2,902.4 miles

    SanFran1 = "SF to vegas"  #569.0 miles
    SanFran2 = "SF to LA"  #381.9 miles
    SanFran3 = "SF to NY"   #2,902.4 miles
    '''


    def __init__(self):
        self.passenger_information = []

    def check_in(self,fname,lname,state_id,id_exp,depart_city,return_city=None):
        #date_today = datetime.today().strftime('%m-%d-%Y')
        conditions = True
        if id_exp <= datetime.today() - timedelta(days=1):
            print('Your license is expired.')
            print('Please update your license in the case of Hyperloop agent inquiry.')
            conditions = True
        
        if conditions == True:
            print('Please check to make sure your information was input correctly.')
            print('Please be sure to check the date of your trip/s to verify it is correct.')
            print('Your ticket is ready for credit card purchase.')
            TransportCheckIn.total_trips += 1
            self.passenger_information = [fname,lname,state_id,id_exp]

    


class HyperloopLA(TransportCheckIn):
    
    #Route-108 is Los Angeles to Las Vegas
    def route108_calculate(self):
        pass
    #Route-208 is Los Angeles to San Francisco
    def route208_calcluate(self):
        pass
    #Route-301 is Los Angeles to New York
    def route301_calculate(self):
        pass
        
    def roundtrip_calculate(self):
        pass
        



Copyright-Donald Kaiser
