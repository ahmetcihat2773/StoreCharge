import calendar
from datetime import datetime
import random
class ChargingStation():
    def __init__(self,charger_type,store_hours,tenant_exception,store_exception):
        """
        charger can be used public or privat for the managers.
        """
        print("CharcingStation is Initialized")
        self.tenant_exception = tenant_exception
        self.store_exception = store_exception
        self.store_hours = store_hours
        self.charger_type = charger_type
        self.exception = []
    def open_close(self,timeStamp):
        """
        Check whether the station is open within this period of time
        """
        day_number = timeStamp.weekday()
        day_name = calendar.day_name[day_number]
        hour = timeStamp.hour
        minute = timeStamp.minute
        open_close_time = self.conver2time(self.store_hours[day_name])
        print("week day",day_name)
        for times in open_close_time: 
            print(times)          
            if (hour >= times[0].hour and minute >= times[0].minute) and (hour <= times[1].hour):
                return True
            elif (hour >= times[0].hour and minute >= times[0].minute) and (hour == times[0].hour and minute < times[0].minute):
                return True    
        return False
        
    def conver2time(self,string_time):
        """
        Convert string to hour and minute
        """
        print(string_time)
        tempList = []
        for times in string_time:
            tempList.append([datetime.strptime(times[0],"%H:%M"),datetime.strptime(times[1],"%H:%M"),])
        return tempList
        


    def closes_open_close(self):
        """
        Return the close status change from open to closed vice versa.
        """        
    def check_exception(self):
        if self.exception:
            return self.exception
        elif self.store_exception:
            return self.store_exception
        elif self.tenant_exception:
            return self.tenant_exception
        else:
            return False
