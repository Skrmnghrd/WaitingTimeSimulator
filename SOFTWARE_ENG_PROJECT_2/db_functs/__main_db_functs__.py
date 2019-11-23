#library imports
import MySQLdb
#===================
#local imports
from AddCustomer import xAddCustomer
from GetCustomers import xGetCustomer
from AddCashier import xAddCashier
#from AddCashier import __AddCashier
#from GetCustomers import  __getCustomers



class db_functions(xAddCustomer, xGetCustomer, xAddCashier): #, __add_cashier__, __get__customers): 
  #don't forget to inehrit your heirloom
  def __init__(self):
    """
    Initialize the vars and then re-initite the superclasses
    #is this the right way to do it? it's my first time ;> but hey, big break!
    """
    
    #I GOT STUCK FOR 2 HOURS BEACUSE OF THE FREAKING DUNDER. linti nga biga 
    #wala gd pulosf bighfiub iuyg h v ouib

    #yot nga linte ni, didto i init ang db kada himo mo ka object dputa kasuluya
    #or himo ka wrapper
    #AddCustomer.__AddCustomer.__init__() #na init ya na gani dpita
    #print(dir(__AddCustomer))

    #__add_cashier__.__init__(self)
    #__get__customers.__init__(self)

    self.db = MySQLdb.connect(host='localhost',
                    user='root',
                    password='talablasani',
                    db='software_project_two') 
    #don't touch this self.db since we're calling db.commit on sublibraries

    self.cur = self.db.cursor()   

    xAddCustomer.__init__(self, self.cur)
    xGetCustomer.__init__(self, self.cur)
    xAddCashier.__init__(self, self.cur)

  def add_customer(self):
    """
    gets the parameters and adds customer to database
    """

    print('Add Customer')
    self.generate_customer()

  def add_cashier(self):
    """
    adds_cashier to the database
    """
    print('cashier generated')
    self.generate_cashier()

  def get_customers(self):
    """
    gets the customer $select * from cust order by entry time
    data= ['id','entry_time','time_done','date','served_by']
    """
    return(self.fetch_customers())
  
  
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