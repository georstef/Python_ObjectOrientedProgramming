import sys

class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers")
        if integer % 2 != 0: # same same => if integer % 2:
            raise ValueError("Only evens")
        super().append(integer)


def no_return():
  print("I am about to raise an exception")
  #raise Exception("This is always raised")
  raise ValueError("This is always raised")
  print("This line will never execute")
  return "I won't be returned"

def call_exceptor():
  print("call_exceptor starts here...")
  try:
    no_return()
  except ZeroDivisionError:
      print('ZeroDivisionError')
  except ValueError:
      print('ValueError')
  except BaseException:
      print('Base Exception')
  finally:
    print('finally')

  print("an exception was raised...so this line won't run")
  
def funny_division2(anumber):
  try:
    if anumber == 13:
      x = [ValueError, Exception, SystemExit, KeyboardInterrupt]
      raise x[1]("13 is an unlucky number", 'error arg1')
    print(100 / anumber)
  except (ZeroDivisionError, TypeError):
    print("Enter a number other than zero")
  except BaseException as e:
    print(e.args[1])
    print("'"+e.__class__.__name__+"' raised")
    sys.exit()
  else:
      print('not a single exception raised')
  finally:
      print('finally')
    
class NewException(Exception):
    pass


class InvalidWithdrawal(Exception):
  def __init__(self, balance, amount):
    super().__init__("account doesn't have ${}".format(amount))
    self.amount = amount
    self.balance = balance

  def overage(self):
    return str(self.amount - self.balance)+'$'

class OutOfStock(Exception):
  def __init__(self, back_in_stock_date):
    super().__init__()
    self.back_in_stock_date = back_in_stock_date
