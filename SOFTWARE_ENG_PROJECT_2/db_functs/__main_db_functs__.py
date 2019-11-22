#library imports
import MySQLdb
#===================
#local imports
from AddCustomer import xAddCustomer
#from AddCashier import __AddCashier
#from GetCustomers import  __getCustomers



class db_functions(xAddCustomer): #, __add_cashier__, __get__customers):

  def __init__(self):
    """
    Initialize the vars and then re-initite the superclasses
    #is this the right way to do it? it's my first time ;> but hey, big break!
    """
    
    self.db = MySQLdb.connect(host='localhost',
                    user='root',
                    password='talablasani',
                    db='software_project_two') 
    
    #I GOT STUCK FOR 2 HOURS BEACUSE OF THE FREAKING DUNDER. linti nga biga 
    #wala gd pulosf bighfiub iuyg h v ouib

    xAddCustomer.__init__(self, self.db)
    #yot nga linte ni, didto i init ang db kada himo mo ka object dputa kasuluya
    #or himo ka wrapper
    #AddCustomer.__AddCustomer.__init__() #na init ya na gani dpita
    #print(dir(__AddCustomer))
    print('awd')
    #__add_cashier__.__init__(self)
    #__get__customers.__init__(self)

  def add_customer(self):
    """
    gets the parameters and adds customer to database
    """
    print('Add Customer')
    self.runme()
    #__add__customer__
    pass
  def add_cashier(self):
    """
    adds_cashier to the database
    """
    pass
  def get_customers(self):
    """
    gets the customer $select * from cust order by entry time
    """
    pass
  
  
if __name__ == "__main__":
    x = db_functions()
    x.add_customer()
"""

class Hello():
  def __init__(self, var1):
    self.var1 = var1
  def funcfromhello(self):
    print(self.var1)
class Test(Hello):
  def __init__(self, var1):
    #found a solution
    Hello.__init__(self, var1)
    """
    

"""

    def __init__(self,num):
        #call the superclass again to init it
        Num.__init__(self,num)
        self.n2 = num*2
        """

"""
    pass
"""