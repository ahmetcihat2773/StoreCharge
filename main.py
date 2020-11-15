from Tenant import Tenant
from datetime import datetime
import csv
import random
class main():
    def __init__(self):
        print("MAIN is started")
        self.tenants = {}
    def register_tenant(self):
        """
        Create a new Tenant.
        """
        if bool(self.tenants):
            print(bool(self.tenants))
            self.tenants[max(list(self.tenants.keys()))+1] = Tenant()
        else: 
            self.tenants[0] = Tenant()
    def check_exception_time(self,check_time,exception):
        print(exception)
        if exception[0][0] <= check_time <= exception[0][1] and exception[0][2] == "Open":
            print("Open")
            return True
        else:
            return False
        #self.exception.append([start_time,end_time,open_or_close])
    def read_exceptions(self):
        with open('exception_file.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
            
                exception_start = datetime.strptime(row[3],"%Y/%m/%d %H:%M:%S")
                exception_end = datetime.strptime(row[4],"%Y/%m/%d %H:%M:%S")
                if int(row[5]) == 0:
                    if self.tenants[int(row[0])].exception:
                        self.tenants[int(row[0])].exception.pop()
                    self.tenants[int(row[0])].exception.append([exception_start,exception_end,row[6]])        
                elif int(row[5]) == 1:
                    store_exception = self.tenants[int(row[0])].stores[int(row[1])].exception
                    if store_exception:
                        store_exception.pop()
                    store_exception.append([exception_start,exception_end,row[6]])
                else:
                    charger_exception = self.tenants[int(row[0])].stores[int(row[1])].charger[int(row[2])].exception
                    if charger_exception:
                        charger_exception.pop()
                    charger_exception.append([exception_start,exception_end,row[6]])

    def show_entities(self,tenant_id,store_id,charger_id):
        print(isinstance(store_id, int))
        if type(tenant_id) == int and type(store_id) == int and type(charger_id) == int:
            print("TENANT ID: ",tenant_id)
            print("STORE ID: ",tenant_id)
            print("CHARGER ID:",charger_id)
            print("CHARGER EXCEPTION:",self.tenants[tenant_id].stores[store_id].charger[charger_id].exception)
        elif type(tenant_id) == int and type(store_id) == int and not type(charger_id) == int:
            print("TENANT ID: ",tenant_id)
            for store_id in self.tenants[tenant_id].stores.keys():
                print("STORE ID:", store_id)
                print("STORE EXCEPTION:", self.tenants[tenant_id].stores[store_id].exception)
            print("store_id")
        elif type(tenant_id) == int and not type(store_id) == int:
            print("TENANT ID: ",tenant_id)
            print("TENANT EXCEPTION: ",self.tenants[tenant_id].exception)


    def app_loop(self):
        #self.create_exception_file()    
        self.register_tenant()
        print("Tenants: ",self.tenants)
        self.register_tenant()
        print("Tenants: ",self.tenants)
        self.read_exceptions()
        while True:
            print("Press 1 Ask a charger is closed or not","\nPress 2 Learn the closest opening and closing time")
            print("Press 3 Select Tanent","\nPress 4 Select Store","\nPress 5 Select Charge Station","\nPress 0 To exit")
            x = int(input())
            if x == 0:
                break
            elif x == 1:
                print("Enter the Tenant ID")
                self.tenant_id = input()
                print("Exception start date in from day/month/year hour/minute")
                start_time = input()
                start_time = datetime.strptime(start_time, "%d/%m/%Y %H:%M")
                print("Exception end date in from day/month/year hour/minute")
                end_time = input()
                end_time = datetime.strptime(end_time, "%d/%m/%Y %H:%M")
                self.tenants[self.tenant_id].create_exception()
            elif x == 2:
                print("Enter the Tenant ID")
                self.tenant_id = int(input())
                print("Enter the Store ID")
                self.store_id = int(input())
                #Ask here the Store Id
                print(self.tenants[self.tenant_id].stores)
                self.tenants[self.tenant_id].stores[self.store_id].define_exception()
            elif x == 3:
                self.read_exceptions()
                print("Enter Tenant ID")
                self.tenant_id = int(input())
                self.show_entities(self.tenant_id,False,False)
            elif x == 4 :
                self.read_exceptions()
                print("Enter Tenant ID")
                tenant_id = int(input())
                print("Enter Store ID")
                store_id = int(input())
                self.show_entities(tenant_id,store_id,False)
            elif x == 5 :
                self.read_exceptions()
                print("Enter Tenant ID")
                tenant_id = int(input())
                print("Enter Store ID")
                store_id = int(input())
                print("Enter Charger ID")
                charger_id = int(input()) 
                self.show_entities(tenant_id,store_id,charger_id)    
            elif x==6:
                print("Enter Tanent ID\nThese are the tanent IDs")
                print(self.tenants.keys())
            elif x == 7:
                for tenant_id in self.tenants.keys():
                    print(tenant_id,"has the",self.tenants[tenant_id].keys())
            elif x == 8:
                for tenant_id in self.tenants.keys():
                    for store_id in self.tenants[tenant_id].keys():
                        print("TENANT IDs: ",tenant_id," Store IDs: ", store_id, "Charger IDs: ",self.tenants[tenant_id][store_id].charger)
        
    def create_exception_file(self):
        with open('exception_file.csv', mode='w',newline='') as exception_file:
            exception_file = csv.writer(exception_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            exception_file.writerow(["tenant_id","store_id","charger_id","Start_time","End_time","Exception_Type"])
            for tenat_id in range(0,2):
                for store_id in range(0,4):
                    for charger_id in range(0,4):
                        exception_type = random.randint(0,2)
                        start_time,end_time = self.random_datetime()
                        if exception_type == 0:
                            exception_file.writerow([str(tenat_id),"None","None",start_time,end_time,str(exception_type)])
                        elif exception_type == 1 :
                            exception_file.writerow([str(tenat_id),str(store_id),"None",start_time,end_time,exception_type])
                        else:
                            exception_file.writerow([str(tenat_id),str(store_id),charger_id,start_time,end_time,exception_type])
    def random_datetime(self):
        year = 2020
        month = random.randint(8,12)
        day = random.randint(5,25)
        hour = random.randint(0,23)
        minute = random.randint(0,59)  
        second = random.randint(0,59)
        start_time = datetime(year,month,day,hour,minute,second)
        start_time = start_time.strftime("%Y/%m/%d %H:%M:%S")
        month = random.randint(month,12)
        day = random.randint(day,25)
        hour = random.randint(hour,23)
        minute = random.randint(minute,59)  
        second = random.randint(second,59)
        end_time = datetime(year,month,day,hour,minute,second)
        end_time = end_time.strftime("%Y/%m/%d %H:%M:%S")
        return start_time,end_time
main = main()
main.app_loop()