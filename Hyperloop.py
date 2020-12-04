from datetime import datetime, timedelta
import time
import math

class Hyperloop(object):
    '''This class is to store data pertaining to ticket purchases 
    for the Hyperloop train created by Elon Musk. 
    '''
    vehicle = 'Hyperloop'
    
    def __init__(self,start_route,rnum):
        self.start_route = start_route
        self.route_num = rnum

    def __unicode__(self):
        return self.show()

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def show(self):
        if self.route_num == 105:
            rnum = "105 to VG-04"
        elif self.route_num == 290:
            rnum = "105 to SF-109"
        elif self.route_num == 387:
            rnum = "387 to NY-45"
        else:
            rnum = self.route_num
        return "Route-{}. Departing from {}.".format(rnum,self.start_route)

    
class DTLA19_Routes(object):
    def __init__(self):
        self.dtla19_routes = []
        self.dtla19_dists = []
        self.build_dtla19()

    #shows all routes for the Downtown Los Angeles Hyperloop Station
    def show(self):
        [print(route.show()) for route in self.dtla19_routes]

    #Create a new route by simply inputing route info in the list below as follows: 290-to-SanFran-SF509 (382.9 mi)
    def build_dtla19(self):
        '''DTLA-19 Union Station'''
        self.dtla19_routes = []
        for route in ['DTLA-19 Union Station']:
            for rnum in ['290-to-SanFran-SF509 (382.9 mi)', '387-to-PortOR-PRT691 (962.2 mi)']:
                self.dtla19_routes.append(Hyperloop(route,rnum))


class Vegas04_Routes(object):
    def __init__(self):
        self.vg04_routes = []
        self.build()

    #shows all routes for the current Hyperloop route_num
    def show(self):
        [print(route.show()) for route in self.vg04_routes]

    #Creates a new route by simply inputing route in the list
    def build(self):
        '''Vegas Station-04 Routes'''
        self.vg04_routes = []
        for route in ['Vegas-VG04']:
            for rnum in ['200-ti-SanFran-SF509 (570.3 mi)', '300-to-LA-DTLA19 (270.3 mi)', '400-to-PortOR-PRT691 (974.6 mi)']:
                self.vg04_routes.append(Hyperloop(route,rnum))



class Passenger(object):
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
    def passengerInfo(self):
        print("Passenger name is {} {}".format(self.fname,lname))
        return self


    




#goulash = Hyperloop("DTLA-19",105)
#print(goulash.show())
goulash2 = DTLA19_Routes()
goulash2.show()
goulash3 = Passenger('David', 'Anthony')
#print(goulash3.passengerInfo)










#if __name__ == "__main__":
   #Trans_obj = TransportCheckIn()
