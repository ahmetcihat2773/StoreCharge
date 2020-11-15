import calendar
from datetime import datetime
import random
class ChargingStation():
    def __init__(self,store_hours,tenant_exception,store_exception):
        """
        charger can be used public or privat for the managers.
        """
        print("CharcingStation is Initialized")
        self.tenant_exception = tenant_exception
        self.store_exception = store_exception
        self.store_hours = store_hours
        self.exception ={}
    def check_open_closed(self,timeStamp):
        """
        Check whether the station is open within this period of time
        """
        print(timeStamp)
        dateTime = datetime.fromtimestamp(timeStamp)
        print(dateTime)
        day_number = dateTime.weekday()
        day_name = calendar.day_name[day_number]
        hour_only = dateTime.time()
        print("week day",day_name)
        if bool(self.exception):
            print("Charger Exception")
            print(self.exception)
            result = self.exception_checker(self.exception,dateTime)
        elif bool(self.store_exception):
            print("Store Exception")
            print(self.store_exception)
            result = self.exception_checker(self.store_exception,dateTime)
        elif bool(self.tenant_exception):
            print("Tenant Exception")
            print(self.tenant_exception)
            print(self.exception_checker(self.tenant_exception,dateTime))
            result = self.exception_checker(self.tenant_exception,dateTime)    
        if result == "open":
            return True
        elif result == "closed":
            return False
        elif result =="out_of_range":
            # Look at the normal time
            print(self.store_hours)
            print("WORKING HOURS ON "+day_name,self.store_hours[day_name])
            time_only = dateTime.time()
            for working_pair in self.store_hours[day_name]:
                # Working time : 7.30 - 12.35,  Looking for 7.25
                if  working_pair[0] < time_only and time_only < working_pair[1]:
                    return True
                else:
                    return False

               



    def exception_checker(self,exception,dateTime):
        if exception["start"] <= dateTime and dateTime < exception["end"]:
            if exception["type"] == "closed":
                return "closed"
            else:
                return "open"
        return "out_of_range" 
    def conver2time(self,string_time):
        """
        Convert string to hour and minute
        """
        print(string_time)
        tempList = []
        for times in string_time:
            tempList.append([datetime.strptime(times[0],"%H:%M"),datetime.strptime(times[1],"%H:%M"),])
        return tempList
        


    def closes_open_close(self,timespan):
        """
        Return the close status change from open to closed vice versa.
        """        


        """

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
