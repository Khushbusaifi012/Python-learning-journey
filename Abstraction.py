from abc import ABC,abstractmethod
class Bankapp(ABC):
    def database(self):
        print("connected to database")
    
    @abstractmethod
    def security(self):
        pass

class MobileApp(Bankapp):
    def mobile_login(self):
        print("login into mobile")
    
    def security(self):
        print("mobile security")
    
mob=MobileApp()
mob.database()
mob.security()
mob.mobile_login()