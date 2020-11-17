from ChargingStation import ChargingStation
import random
from datetime import datetime,time
class Store():
    def __init__(self,charger_number,tenantException):
        """
        Chargers needs to work at the same time with the store opening hours.
        """
        self.tenant_exception = tenantException
        self.charger_number = charger_number
        # Working hours of store
        self.store_hours = {}
        self.store_hours["Monday"] = self.random_time(random.randint(1,3)) 
        self.store_hours["Tuesday"] = self.random_time(random.randint(1,3))
        self.store_hours["Thursday"] = self.random_time(random.randint(1,3))
        self.store_hours["Wednesday"] = self.random_time(random.randint(1,3))
        self.store_hours["Friday"] = self.random_time(random.randint(1,3))
        self.store_hours["Saturday"] = self.random_time(random.randint(1,3))
        self.store_hours["Sunday"] = self.random_time(random.randint(1,3))
        self.charger = {}
        self.exception = {}
        for i in range(self.charger_number):            
            self.charger[i] = ChargingStation(self.store_hours,self.tenant_exception,self.exception)
            
    def random_time(self,num_daysplit):    
        hour = 0
        minute = 0
        time_temp_list = []
        time_list = []
        flag = True
        while flag:    
            try:
                for n in range(num_daysplit):
                    for i in range(2):    
                        hour = random.randint(hour,24)
                        minute = random.randint(minute,60)
                        date_time = time(hour=hour,minute=minute)
                        time_temp_list.append(date_time)
                    time_list.append(time_temp_list)
                    time_temp_list = []
                flag = False
            except:
                time_list = []
                time_temp_list = []
                hour = 0
                minute = 0
                continue
        return time_list


