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



#import sys
#sys.path.insert(0, "Users/paulo/Desktop/SOFTWARE_ENG_PROJECT_2/simulator/")



import random
#from AddCashier import __AddCashier
#from GetCustomers import  __getCustomers



class db_functions(xAddCustomer,
                   xGetCustomer, 
                   xAddCashier,
                   xErradicator, 
                   xGetCashiers,
                   xQueCustomers,
                   xCloseTransaction,
                   

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
      self.waiting_time = 0 #tuple (min, max) (2, 5)
      self.cashier_amount = 0 #int how many cashiers
      self.customers = 0 
      self.operating_time = 0


    finally:
      pass
    #don't touch this self.db since we're calling db.commit on sublibraries

    self.cur = self.db.cursor()   

    xAddCustomer.__init__(self, self.cur)
    xGetCustomer.__init__(self, self.cur)
    xAddCashier.__init__(self, self.cur)
    xErradicator.__init__(self, self.cur)
    xGetCashiers.__init__(self, self.cur)
    xQueCustomers.__init__(self, self.cur)
    xCloseTransaction.__init__(self, self.cur)
    #xSimulate.__init__(self, self.cur)

  def add_customer(self):
    """
    gets the parameters and adds customer to database
    """
    
    
    for i in range(random.randrange(self.customers[0], self.customers[1])):
      self.generate_customer()
    print('Customer Added')
    
  def add_cashier(self):
    """
    adds_cashier to the database
    """
    for i in range(self.cashier_amount):
      self.generate_cashier()
    
    print("Cashier Added")

  def get_table_names(self):
    """
    won't try to put this on another file since I don't have much time now :> it's gonna be thanks giving tomorrow 
    """

    self.cur.execute("SHOW TABLES")
    return(self.cur.fetchall())


  def fetch_table_columns(self, table):

    self.cur.execute("DESCRIBE {}".format(table))
    
    return([x[0] for x in self.cur.fetchall()])


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
    #print('customer q-ed')

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
    #throws an error over here when the transaction ends :> please fix, your'er almost there
    self.end_transaction(cashier_uuid, customer_uuid, current_time)
    #print('Transaction Closed')



  def get_lowest_cust(self, current_time):
    """
    gets the customer with the lowest time_entry that's not yet in the que
    #get's the next recent one #well just to be safe, we'll query the heck out of this lol
    """
    self.cur.execute("""select * from customers where customers_entry_time <= {0} and customer_uuid not in (select cashier_q_cust_uuid from cashier_queue) and customer_service_needed != 0 ORDER BY customers_entry_time;""".format( int(current_time)) ) #well, this returns none if all are inside the queing now so
    row = self.cur.fetchall()
    return(row)
  
  def get_least_loaded_cashier(self):
    """Returns a list of list with the number of customers on each of the cashiers queue
    """
    self.cur.execute("""select cashier_uuid from cashier""")
    cashier_pool = self.cur.fetchall()
    cashier_pool = [list(x) for x in cashier_pool] #lists of cashiers
    for index, cashier_uuid in enumerate(cashier_pool):
      
      self.cur.execute(""" select count(*) from cashier_queue where cashier_q_cashier_uuid='{0}' """.format(cashier_uuid[0]))
      count = self.cur.fetchone()#it's only one
      if count == None:
        cashier_pool[index].append(0)
      cashier_pool[index].append(count[0])
      
    cashier_pool = sorted(cashier_pool, key=itemgetter(1))  #returns the first guy that has the lowest peopl in the q
    
    return cashier_pool

  def get_customer_service_time(self, customer_uuid):
    self.cur.execute("""select customer_service_needed from customers where customer_uuid='{0}'""".format(customer_uuid))
    return self.cur.fetchone() 

  def cashier_work(self, cashier_uuid, current_time):
    #get the working time first if it's 1, close transaction

    get_the_customer_being_served= """select customer_uuid FROM customers WHERE customer_uuid in (select cashier_q_cust_uuid from cashier_queue where cashier_q_cashier_uuid='{0}') ORDER BY customers_entry_time LIMIT 1""".format(cashier_uuid[0])
    #somethign wrong over here
    #only returns the first customer, explains why the customer doesn't change
    
    self.cur.execute(get_the_customer_being_served)
    customer_uuid = self.cur.fetchall() #error over here
    #customer uuid is actually the whole row
    #please edit #go to sleep
    customer_uuid = customer_uuid[0][0]
     
    service_time = self.get_customer_service_time(customer_uuid)[0]
    
    print('SERVICE TIME UNTOUCHED: ' + str(service_time))

    if (((service_time - 1) < 1 and (service_time - 1) > 0 ) or (service_time -1 == 0)) or (service_time > 0 and service_time < 1): #means its 0.01 - 0.99
      #change this to 
      #service_time is -1 is less than 1 but not 0 then
      #wait for it to close then

      #get the customer being served on your queue if exists
      #deduc the remaining time from him if get the customer_being served is not none
      #print('servtime = :' + str(service_time))
      current_time += (service_time - 1)
      #print('current_time = :' + str(current_time))
       #where service time is a decimal or flaot or service time is 1
      self.close_transaction(cashier_uuid,customer_uuid,current_time)
      self.cur.execute(get_the_customer_being_served)
      check_q = self.cur.fetchall()

      if len(check_q) != 0: #if there's no one in the q, don't pass the remaining float numbers to the next person
      #wala tao sa linya, what can u xpect right? lol
        if service_time > 1:
          customer_uuid = self.cur.fetchall()
          customer_uuid = customer_uuid

          self.cur.execute(""" UPDATE customers SET customer_service_needed=(customer_service_needed - {0}) WHERE customer_uuid='{1}'""".format((service_time -1 ), str(customer_uuid) ))
          self.db.commit()

        else:
          customer_uuid = self.cur.fetchall()
          customer_uuid = customer_uuid

          self.cur.execute(""" UPDATE customers SET customer_service_needed=(customer_service_needed - {0}) WHERE customer_uuid='{1}'""".format((service_time), str(customer_uuid) ))
          self.db.commit()



    else: #well if it ain't one then
      #error now is over here lol I just woke up niggguhhhs!
      self.cur.execute(""" UPDATE customers SET customer_service_needed={0} WHERE customer_uuid='{1}'""".format( (service_time -1 ), str(customer_uuid) ))
      #THIRTY FREAKING MINUTES OF LOOKING FOR THAT (INT UP THERE) #was wondering why it's not floating
      self.db.commit()

  def get_cashiers_that_have_people_in_line(self): #goddamn that function name was longer than I thought lol
    self.cur.execute('select DISTINCT cashier_q_cashier_uuid from cashier_queue')
    return self.cur.fetchall()



  def import_sql_to_database(self):
    pass

  def check_null(self):
    self.cur.execute('select DISTINCT cashier_q_cashier_uuid from cashier_queue')
    return self.cur.fetchall()
if __name__ == "__main__":
  #x = db_functions()
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