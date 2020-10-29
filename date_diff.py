from datetime import datetime as dd, date
from dateutil.parser import parse
import pendulum

class Date_Diff:
    def __init__(self, d2):
        self.d2 = d2      

    
    def days_between(self):
        now = pendulum.now('Europe/London')
        now = now.to_iso8601_string()
        now = pendulum.parse(now)
        print(now) 
        print(self.d2)            
        """d1 = now     
        d2 = self.d2
        return abs((d2 - d1).days) """ 
        return 1      


print(Date_Diff.days_between("2020-10-27T22:02:07.091Z"))