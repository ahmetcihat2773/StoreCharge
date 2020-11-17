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
        => What happen if there is no exception.
        
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
    def exception_working_hour_checker(self,exception,working_hour):
        # working_hour : list of time
        # exception is a dictionary : "start","end","type" keys.
        year = exception.year
        month = exception.month
        day = exception.day
        date = year+"/"+month+"/"+day
        print(self.store_hours[day_name])
        working_time = working_pair.strftime("%H:%M:%S")
        working_date = datetime.strptime(date+" "+working_time,"%Y/%m/%d %H:%M:%S")
        print(working_date)
        """
        for working_pair in self.store_hours[day_name]:
            # Working time : 7.30 - 12.35,  Looking for 7.25
            working_time = working_pair.strftime("%H:%M:%S")
            working_date = datetime.strptime(date+" "+working_time,"%Y/%m/%d %H:%M:%S")
            if exception["end"] - working_date >0:

                return True
        return False
        """
    def where_is_datetime(self,exception,dateTime):
        """
        return if the dateTime time is lower than exception start, or in the middle of the exception or after end of exception
        """
        if dateTime < exception["start"]:
            return "left"
        elif exception["start"] <= dateTime and dateTime < exception["end"]:
            return "middle"
        elif dateTime > exception["end"]:
            return "right"
    def nextday_name(self,day_number):
        """
        returns a list of working hours of the store for a spe
        """
        day_number += 1
        day_name = calendar.day_name[day_number]
        return day_name 





    def isbetween(self,charger_exception,dateTime):
        """
        This function returns the datetime object soonest to the given dateTime.

        """
        dateTime_date = charger_exception["start"].date()
        dateTime_day = dateTime.day
        if bool(charger_exception):
            if charger_exception["start"].date() < dateTime.date() and dateTime.date() < charger_exception["end"].date():    
                for time_pair in self.store_hours[dateTime_day]:              
                    time_pair[0] = datetime.combine(date)
                    if charger_exception["start"].time() > working_pair[0] and charger_exception["end"].time() < working_pair[1]:
                        if dateTime.hour() < time_pair[0]:
                                return datetime.combine(dateTime_date,time_pair[0])
                        elif dateTime.hour() > time_pair[0] and dateTime.hour() < charger_exception["start"].hour():
                            if charger_exception["type"] == "closed":
                                return charger_exception["start"]
                            else:
                                return datetime.combine(dateTime_date,time_pair[1])
                        elif dateTime > charger_exception["start"] and dateTime < charger_exception["end"]:
                            if charger_exception["type"] == "closed":
                                return charger_exception["end"]
                            else:
                                return time_pair[1]
                        elif dateTime > charger_exception["end"] and dateTime < time_pair[1]:
                            if charger_exception["type"] == "closed":
                                return time_pair[1]
                    if charger_exception["start"].time() > working_pair[0] and charger_exception["end"].time() > working_pair[1] and  charger_exception["start"].time() < working_pair[1]:
                        if dateTime < time_pair[0]
            
            """
            
            dateTime_place = self.where_is_datetime(charger_exception,dateTime)
            if charger_exception["type"] == "open":                
                if dateTime_place == "left":
                    return charger_exception["start"]
                elif dateTime_place = "middle":
                    return charger_exception["end"]
                else:
                    day_name = self.nextday_name(dateTime.week_day())
                    dateTime_time = dateTime.time()
                    # compare the times first.
                    date = dateTime.strftime("%Y/%m/%d")
                    #dateTime = date+" "+self.store_hours[day_name][0][0].strftime("%H:%M:%S")
                    for time_pairs in self.store_hours[day_name]:
                        if dateTime_time < time_pairs[0]:
                            time_only = time_pairs[0].strftime("%H:%M:%S")
                            dateTime = date+" "+time_only
                            return dateTime
                        elif time_pairs[0] < dateTime_time and dateTime_time < time_pairs[1]:
                            time_only = time_pairs[].strftime("%H:%M:%S")
                            dateTime = date+" "+time_only
                        elif dateTime_time > time_pairs[1]:
                            # return the starting time of tomorrow.
                            day_name = self.nextday_name(dateTime.week_day())
                            date = dateTime.strftime("%Y/%m/%d")
                            dateTime = date+" "+
                            return dateTime
            
            
            
            
            
            
            
            
            
            
            
            else:
                if charger_exception["type"] == "closed":                
                    if dateTime_place == "left":
                        day_number = dateTime.week_day()
                        day_name = calendar.day_name(day_number)
                        self.exception_closed(dateTime,day_name)
                    elif dateTime_place = "middle":
                        return charger_exception["end"]
                    else:
                        # return the starting time of tomorrow.
                        day_name = self.nextday_name(dateTime.week_day())
                        date = dateTime.strftime("%Y/%m/%d")
                        dateTime = date+" "+self.store_hours[day_name][0][0].strftime("%H:%M:%S")
                        return dateTime


        
        if bool(store_exception):
            """   


    def soonest_open_close(self,timeStamp):
        """
        convert timestamp into datetime.
        check if there is a exception.
        """
        print("Timestamp",timeStamp)
        dateTime = datetime.fromtimestamp(timeStamp)
        print("Datetime",dateTime)
        day_number = dateTime.weekday()
        day_name = calendar.day_name[day_number]
        hour_only = dateTime.time()
        print("week day",day_name)
        if bool(self.exception):
            print("Charger Exception")
            print(self.exception)
            result = self.exception_checker(self.exception,dateTime)
            if result == "open":
                if bool(self.store_exception):




                elif bool(self.tenant_exception):


                else:


            elif result == "closed":
                # Which day exception ends. If in that day, normal working hours are valid then check the possible
                # opening hour. If not return the openning hour of tomorrow. 
                if bool(self.store_exception):
            elif result = "out_of_range":
                result = self.exception_checker(self.store_exception,dateTime)
