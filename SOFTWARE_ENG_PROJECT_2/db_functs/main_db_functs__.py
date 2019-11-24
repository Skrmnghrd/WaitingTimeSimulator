#library imports
import MySQLdb
from operator import itemgetter
#===================
#local imports
from AddCustomer import xAddCustomer
from GetCustomers import xGetCustomer
from GetCashiers import xGetCashiers
from AddCashier import xAddCashier
from Erradicator import xErradicator
from QueCustomers import xQueCustomers
from CloseTransaction import xCloseTransaction
import sys
import random
#from AddCashier import __AddCashier
#from GetCustomers import  __getCustomers



class db_functions(xAddCustomer,
                   xGetCustomer, 
                   xAddCashier,
                   xErradicator, 
                   xGetCashiers,
                   xQueCustomers,
                   xCloseTransaction

                   ): #, __add_cashier__, __get__customers): 
  #don't forget to inehrit your heirloom
  def __init__(self, **kwargs):
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

    try:
      self.waiting_time = kwargs['waiting_time'] #tuple (min, max) (2, 5)
      self.cashier_amount = kwargs['cashiers'] #int how many cashiers
      self.customers = kwargs['customers'] #tuple #how many cust (min, max) (80,150)
      self.operating_time = kwargs['time'] #tuple (min, max) (850, 1020) #for lazy reasons just convert it all to min. EG 8:30 (8 * 60) + 30
    except:

      print("""\n
      An Error Occured, please supply the corresponding arguments
      self.waiting_time = kwargs['waiting_time'] #tuple (min, max) (2, 5)
      self.cashier_amount = kwargs['cashiers'] #int how many cashiers
      self.customers = kwargs['customers'] #tuple #how many cust (min, max) (80,150)
      self.operating_time = kwargs['time'] #tuple (min, max) (850, 1020) #for lazy reasons just convert it all to min. EG 8:30 (8 * 60) + 30
      """)
    finally:
      self.waiting_time = 0 #tuple (min, max) (2, 5)
      self.cashier_amount = 0 #int how many cashiers
      self.customers = 0 
      self.operating_time = 0
      
    #don't touch this self.db since we're calling db.commit on sublibraries

    self.cur = self.db.cursor()   

    xAddCustomer.__init__(self, self.cur)
    xGetCustomer.__init__(self, self.cur)
    xAddCashier.__init__(self, self.cur)
    xErradicator.__init__(self, self.cur)
    xGetCashiers.__init__(self, self.cur)
    xQueCustomers.__init__(self, self.cur)
    xCloseTransaction.__init__(self, self.cur)

  def add_customer(self):
    """
    gets the parameters and adds customer to database
    """
    
    
    for i in range(self.customers):
      self.generate_customer()
    print('Customer Added')
    
  def add_cashier(self):
    """
    adds_cashier to the database
    """
    for i in range(self.cashier_amount):
      self.generate_cashier()
    
    print("Cashier Added")

  def get_customers(self):
    """
    gets the customer $select * from cust order by entry time
    data= ['id','entry_time','time_done','date','served_by']
    """
    return(self.fetch_customers())

  def get_cashiers(self):
    """
    Removes all the contents of the databse
    #this might be for the developer's use only,? idk
    """
    return(self.fetch_cashiers())
  
  def que_customer(self, cashier_uuid, customer_uuid):
    """cashier_uuid, and cust_uuid"""
    self.load_customer(cashier_uuid, customer_uuid)
    print('customer q-ed')

  def clear_database(self):
    """
    Removes all the contents of the databse
    #this might be for the developer's use only,? idk
    """
    
    self.erradicate_everyone()
    print('Database Cleared! ')



  #=========================================================================================================
  #db functs for Generator, can be accessed without passing an arg to the init :>
  def close_transaction(self, cashier_uuid, customer_uuid, current_time):

    self.end_transaction(cashier_uuid, customer_uuid, current_time)
    print('Transaction Closed')



  def get_lowest_cust(self):
    """
    gets the customer with the lowest time_entry that's not yet in the que
    #get's the next recent one #well just to be safe, we'll query the heck out of this lol
    """
    self.cur.execute("""select * from customers where customer_uuid not in (select cashier_q_cust_uuid from cashier_queue) ORDER BY customers_entry_time;""")
    row = self.cur.fetchone()
    return_me = {
      'customers_id' : row[0],
      'customers_entry_time' : row[1],
      'customers_time_done' : row[2],
      'customers_date': row[3],
      'customers_served_by': row[4],
      'customer_uuid' : row[5],
      'customer_service_needed' : row[6]
    }
    return(return_me)
  
  def get_least_loaded_cashier(self):
    """Returns a list of list with the number of customers on each of the cashiers queue
    """
    self.cur.execute("""select cashier_uuid from cashier""")
    cashier_pool = self.cur.fetchall()
    cashier_pool = [list(x) for x in cashier_pool]
    for index, cashier_uuid in enumerate(cashier_pool):
      
      self.cur.execute(""" select count(*) from cashier_queue where cashier_q_cashier_uuid='{0}' """.format(cashier_uuid[0]))
      count = self.cur.fetchone()#it's only one
      if count == None:
        cashier_pool[index].append(0)
      cashier_pool[index].append(count[0])
      
    cashier_pool = sorted(cashier_pool, key=itemgetter(1))  
    
    return cashier_pool

if __name__ == "__main__":
  x = db_functions()
  pass






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