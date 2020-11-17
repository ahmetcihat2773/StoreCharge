import calendar
from datetime import datetime,timedelta,time
import random
class ChargingStation():
    def __init__(self,store_hours,tenant_exception,store_exception):
        """
        charger can be used public or privat for the managers.
        """
        self.tenant_exception = tenant_exception
        self.store_exception = store_exception
        self.store_hours = store_hours
        self.exception ={}
    def check_open_closed(self,timeStamp):
        """
        Check whether the station is open within this period of time
        => What happen if there is no exception.
        Burda olan charger exception varsa ona bak yoksa store exception varsa ona yoksa
        tenant a bak oda yoksa normal working hours a bakıyor.
        """
        print(timeStamp)
        dateTime = datetime.fromtimestamp(timeStamp)
        print(dateTime)
        day_number = dateTime.weekday()
        day_name = calendar.day_name[day_number]
        hour_only = dateTime.time()
        print("WEEK DAY:",day_name)
        if bool(self.exception):
            print("EXCEPTION TYPE: Charger")
            print(self.exception)
            result = self.exception_checker(self.exception,dateTime)
        elif bool(self.store_exception):
            print("EXCEPTION TYPE: Store")
            print(self.store_exception)
            result = self.exception_checker(self.store_exception,dateTime)
        elif bool(self.tenant_exception):
            print("EXCEPTION TYPE: Tenant")
            print(self.tenant_exception)
            print(self.exception_checker(self.tenant_exception,dateTime))
            result = self.exception_checker(self.tenant_exception,dateTime)    
        if result == "open":
            return True
        elif result == "closed":
            return False
        elif result =="out_of_range":
            # Look at the normal time
            print("WORKING HOURS ON "+day_name,self.store_hours[day_name])
            time_only = dateTime.time()
            for working_pair in self.store_hours[day_name]:
                # Working time : 7.30 - 12.35,  Looking for 7.25
                if  working_pair[0] < time_only and time_only < working_pair[1]:
                    return True
            return False
    def exception_checker(self,exception,dateTime):
        """
        Check whether entered timestamp is in the exception. Datetime is pass as an argument.
        return "closed" "open" "out_of_range"
        """
        if exception["start"] <= dateTime and dateTime < exception["end"]:
            if exception["type"] == "closed":
                return "closed"
            else:
                return "open"
        return "out_of_range" 
    def soonest_open_close(self,timeStamp):
        """
        convert timestamp into datetime.
        check if there is a exception.
        """
        dateTime = datetime.fromtimestamp(timeStamp)
        day_number = dateTime.weekday()
        day_name = calendar.day_name[day_number]
        print("DATETIME",dateTime)
        print("week day",day_name)
        print("WORKING HOURS",self.store_hours[day_name])
        if bool(self.exception):
            print("Charger Exception")
            print(self.exception)
            result = self.exception_time_check(self.exception,dateTime)
            return datetime.timestamp(result)
        elif bool(self.store_exception):
            print("Store Exception")
            print(self.store_exception)
            result = self.exception_time_check(self.store_exception,dateTime)
            return datetime.timestamp(result)
        
        elif bool(self.tenant_exception):
            print("Tenant Exception")
            print(self.tenant_exception)
            result = self.exception_time_check(self.tenant_exception,dateTime)
            return datetime.timestamp(result)
        else:
            result = self.check_working_hours(dateTime)
            return datetime.timestamp(result)
    def exception_time_check(self,exception_dt,dateTime):
        """
        return the datetime with which open/closed status changes.
        """
        day_number = dateTime.weekday()
        if dateTime < exception_dt["start"] :
            if exception_dt["type"] == "open": 
                return exception_dt["start"]
            else:
                return self.check_working_hours(dateTime)  
        elif exception_dt["start"] < dateTime and dateTime < exception_dt["end"]:
            if exception_dt["type"] == "open":
                return exception_dt["end"]
            else:
                return self.check_working_hours(dateTime)
        else:
            return self.check_working_hours(dateTime)
    def check_working_hours(self,dateTime):
        """
        When dateTime is not inside the exception time, check the store working time.
        """
        day_number = dateTime.weekday()
        day_name = calendar.day_name[day_number]
        dateTime_date = dateTime.date()
        dateTime_time = dateTime.time()
        for working_pair in self.store_hours[day_name]:
            if dateTime_time < working_pair[0]:
                return datetime.combine(dateTime_date,working_pair[0])
            elif working_pair[0] < dateTime_time and dateTime_time < working_pair[1]:
                return datetime.combine(dateTime_date,working_pair[1])
        day_number += 1 
        dateTime_date += timedelta(days=1)
        return datetime.combine(dateTime_date,self.store_hours[day_name][0][0])