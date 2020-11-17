from Store import Store
class Tenant():
    def __init__(self):
        print("Tenant Created")  
        self.exception = {}
        self.stores = {}
        self.define_store(0,3)
        self.define_store(1,3)
    def define_store(self,store_id,total_chargerNum):
        self.stores[store_id] = Store(total_chargerNum,self.exception)
        print(self.stores)

    def define_exception(self,start_time,end_time,open_or_close):
        print("Define Exception") 
        if not self.exception:
            self.exception.pop()
            self.exception.append([start_time,end_time,open_or_close])
        else:
            self.exception.append([start_time,end_time,open_or_close])

        
