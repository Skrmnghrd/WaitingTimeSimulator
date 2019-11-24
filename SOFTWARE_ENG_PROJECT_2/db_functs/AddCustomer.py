import random
import uuid
class xAddCustomer:


    def __init__(self, cur):
        self.cur = cur
    def generate_customer(self):
        """
        File: Add Customer,
        Class: xAddcustomer,
        Method: generate_customer
        """
        """        
        dicty = {
            'customers_entry_time': 800,
            'customers_time_done':  1,
            'customers_served_by': 0
        }"""

        #don't use dict keys since they're not sorted so you get random values lol
        self.cur.execute("insert into customers (customers_entry_time,customers_time_done,customer_uuid,customer_service_needed) VALUES ({0},0,'{1}',{2})".format(\
        random.randint( self.operating_time[0], (self.operating_time[1]) ), 
        str(uuid.uuid4()), 
        random.randint(self.waiting_time[0], self.waiting_time[1] ) ) )#.format(random.randint(481,1020), 0,0,'Nobody' ,random.randint(2, 6) )) 
        #those goddaaaaaaarn table values should'nt be strings, jeeez took me 30 minutes to figure out what's wrong. 

        #print('Imported "add customer"')
        self.db.commit() #ignore the error since it'll run (main db functs is using this to put stuff in the db)
#insert into 'customers' (customers_entry_time, customers_time_done, customers_served_by)