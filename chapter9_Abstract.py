def format_m(m):
    return '0' + m if len(m) == 1 else m

def format_d(d):
    return '0' + d if len(d) == 1 else d

def format_y(y):
    return '20' + y if len(y) == 2 else y

def format_base_cents(base, cents):
    base, cents = (str(x) for x in (base, cents))
    if len(cents) == 0:
        cents = '00'
    elif len(cents) == 1:
        cents = '0' + cents
    digits = []
    for i,c in enumerate(reversed(base)):
        if i and not i % 3:
            digits.append(' ')
        digits.append(c)
    base = ''.join(reversed(digits))
    return base, cents

#----------------------------------------------

class FranceDateFormatter:
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in (y,m,d))
        return("{0}/{1}/{2}".format(format_d(d),format_m(m),format_y(y)))

class USADateFormatter:
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in (y,m,d))
        return("{0}-{1}-{2}".format(format_m(m),format_d(d),format_y(y)))


class FranceCurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = format_base_cents(base, cents)
        return "{0}€{1}".format(base, cents)

class USACurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = format_base_cents(base, cents)
        return "${0}.{1}".format(base, cents)

#----------------------------------------------

class USAFormatterFactory:
    def create_date_formatter(self):
        return USADateFormatter()
    def create_currency_formatter(self):
        return USACurrencyFormatter()

class FranceFormatterFactory:
    def create_date_formatter(self):
        return FranceDateFormatter()
    def create_currency_formatter(self):
        return FranceCurrencyFormatter()

if __name__=='__main__'    :
    country_code = "FR"
    factory_map = {
        "US": USAFormatterFactory,
        "FR": FranceFormatterFactory
        }
    formatter_factory = factory_map.get(country_code)() # returns an xxxFormatterFactory instance
    format_date = formatter_factory.create_date_formatter() # returns an xxxDateFormatter instance
    print(format_date.format_date(2013, 12, 31))
