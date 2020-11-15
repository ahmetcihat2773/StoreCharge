import random
from datetime import datetime,time
import csv
def random_time(num_daysplit):    
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
def create_exception(self,start_time,end_time,open_or_close):
    open_closed = ["Open","Closed"]
    year = 2020
    month = random.randint(1,12)
    day = random.randint(1,30)
    hour = random.randint(1,24)
    minute = random.randint(0,60)  
    second = random.randint(0,60)
    start_time = datetime(year,month,day,hour,minute,second)
    month = random.randint(month,12)
    day = random.randint(day,30)
    hour = random.randint(hour,24)
    minute = random.randint(minute,60)  
    second = random.randint(second,60)
    end_time = datetime(year,month,day,hour,minute,second)
    return [start_time,end_time,open_closed[random.randint(0,1)]]
def read_exceptions():
    with open('exception_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                print(datetime.strptime(row[3],"%Y/%m/%d %H:%M:%S"))
read_exceptions()