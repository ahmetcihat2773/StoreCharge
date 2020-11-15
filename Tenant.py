from Store import Store
class Tenant():
    def __init__(self):
        print("Tenant Created")  
        self.exception = []
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

#{"Monday":list(),"Tuesday":list(),"Wednesday":list(),"Thursday":list(),"Friday":list(),"Saturday":list(),"Sunday":list()}
    def check_exception(self,store_id,charger_id):
        exception = self.stores[store_id].check_exception(charger_id)
        if not exception:
            return exception
        else:
            return self.exception
        


"""
---> Tenant class 
    ---> Different type of grocery or market or whatso ever.
        ---> Each grocery or market can have a lot of charge station 
            ---> Each charge station can have different time schedule to work.
                ---> Time schedule : Five keys with the day names and as value it can be two or more different time span different time.
                    ---> Each time period should have opening or closing event. 
Manager charge station is seperate than normal charge station so they should have a different id.
All of the times can be configurable. 
    --> Bir günün farklı zamanları input olarak verilebileceği gibi, bir günden başka bir güne de geçiş olabilir Mesela : 
        --> from 2020-06-01 06:00 through 2020-06-05 18:00 all charging station of a given store are closed due to construction at the store. 
        --> From 2020-05-20 09:00 through 11:00 a given signle charging station is closed due to planned maintenance. 
    --> Tüm charge istasyonları tek seferde açık veya kapalı zamanlar girilebilir. 
    --> Hepsini seçerek yapılan bir exception da eğer önceden bir station için exception tanımlanmışsa bu öncelik olarak kabul edilir. Exceptionlar
    --> Exception zamanları dolduktan sonra yok olurlar ve charge stationlar opening hourslarının yanında exceptionları vardır ve bu exceptionlar
        ilk önce kontrol edilmelidir.  
    --> Kullanıcı bir date time girdiğinde otomatik olarak gün buradan çekilir ve o gün içerisindeki saatler le karşılaştırılır user girdiği saat ve
        eğer charge istasyonu açıksa true yoksa false dönderilir.

    ======>>>>>>  TIMESTAMP e göre yapılacak sistem unutma =================<<<<<<<<<<<<<
"""