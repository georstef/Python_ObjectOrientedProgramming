import datetime

class AgeCalculator:
    def __init__(self, birthday):
        #birthday = YYYY-MM-DD
        self.year, self.month, self.day = (int(x) for x in birthday.split('-'))

    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split('-'))
        age = year-self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age


class AgeCalculatorAdapter:
    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self._calculator = AgeCalculator(birthday)
        
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def get_age(self, date):
        date = self._str_date(date)
        return self._calculator.calculate_age(date)

#a class that extends datetime.date type
class AgeableDate(datetime.date):
    #overrides date.split
    def split(self, char):
        return self.year, self.month, self.day

if __name__=="__main__":
    #with string
    agec = AgeCalculator('1976-09-28')
    print(agec.calculate_age('2013-11-1'))
    
    #with date (use Adapter object)
    agecA = AgeCalculatorAdapter(datetime.date(1976, 9, 28))
    print(agecA.get_age(datetime.date.today()))

    #with an overriden class of datetime.date    
    b = AgeableDate(1976, 9, 28)
    t = AgeableDate.today()
    a = AgeCalculator(b)
    print(a.calculate_age(t))
