import pandas as pd
#For route information dict to convert to str in order to write to a txt file

class dtla19_routes():
    '''DTLA-19 @ Union Station Downtown Los Angeles'''

    route_1 = {"290-to-SanFran-SF509":7}
    route_2 = {"387-to-PortOR-PRT691":8}
    route_3 = {"498-to-ManNY-GrandCentralTerminal":11}

    all_routes = {"290-to-SanFran": 382.9, 
                "387-to-PortOR": 962.2, 
                "498-to-NY-GrandCentralTerminal": 2791.4}
    
    
    route_prices = {"290-to-SanFran-SF509":7,
                    "387-to-PortOR-PRT691":8,
                    "498-to-ManNY-GrandCentralTerminal":11
                    }

    route_information = {"\n290-to-SanFran-SF509":"\nRoute Start Location:  DTLA-19 Downtown Los Angeles @ Union Station.\nRoute End Destination: San Francisco station SF509.\nPrice = $7.00\nDistance = 382.9 mi\n\n",
                         "\n387-to-PortOR-PRT691": "\nRoute Start Location:  DTLA-19 Downtown Los Angeles @ Union Station\nRoute End Destination: Portland Oregon station PRT691.\nPrice = $8.00\nDistance = 962.9 mi\n\n",
                         "\n498-to-ManNY-GrandCentralTerminal": "\nRoute Start Location:  DTLA-19 Downtown Los Angeles @ Union Station\nRoute End Destination: Manhattan New York @ Grand Central Station Terminal.\nPrice = $11.00\nDistance = 2791.4 mi\n\n"
                        }
    
    hyperloop = 'Downtown Los Angeles @ Union Station - DTLA-19'

    def __init__(self):
        self.route_info = []
        
        
    def print_routes(self):
        conditions = True
        if conditions == True:
            self.route_info = self.all_routes
            for key,value in self.all_routes.items():
                (pd.DataFrame.from_dict(data=self.route_information, orient='index').to_csv('DTLA-19.txt', header=False))

    @property
    def show_distance(self):
        for key,value in self.all_routes.items():
            print('Total distance for {} from DTLA-19 is {} miles.'.format(key,value))

    @property
    def show_price(self):        
        for key,value in self.route_prices.items():
            print('The cost for {} is ${}'.format(key,value))

    def __repr__(self):
        return f'{self.show_distance()},{self.show_price()}'

    def __unicode__(self):
        return f'{self.show_distance()},{self.show_price()}'
            
    def __str__(self):
        return f'{self.show_distance()}{self.show_price()}'

          
        
