import sys

#custom import paths
sys.path.insert(0, "../db_functs")
from main_db_functs__ import db_functions

class xSimulate(db_functions):

    def __init__(self, cur):
        self.cur = cur

        db_functions.__init__() #don't pass any args since we're just here to use db_functs to extract.
        #select * from customers where customer_uuid not in (select cashier_q_cust_uuid from cashier_queue) 
        #to filter the ones not in que
        #select count(*) from table

    def commence_simulation(self, time_open=850, closing_time=1300):
        time_open = time_open
        while time_open < closing_time:
            time_open += 1
            next_cust = self.get_lowest_cust() #returns a dict
            if next_cust['customers_entry_time'] >= time_open:
                #sulod sa q
                lowest_cashier_uuid = self.get_least_loaded_cashier()[0][0] #get the lowest cashier
                self.que_customer(lowest_cashier_uuid,next_cust)
                #self.cur.execute("""insert into cashier_queue (cashier_q_cashier_uuid, cashier_q_cust_uuid)""")
                

        #self.cur.execute("insert into cashier_queue (cashier_q_cashier_uuid, cashier_q_cust_uuid) VALUES ('{0}','{1}')".format( cashier_uuid, customer_uuid) )
        #self.db.commit() 
        #pasensya gid, kinanglan ko lg mag una anay subong.