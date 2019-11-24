import sys

#custom import paths

from main_db_functs__ import db_functions

class xSimulate(db_functions):

    def __init__(self, cur):
        self.cur = cur

        db_functions.__init__(self) #don't pass any args since we're just here to use db_functs to extract.
        #select * from customers where customer_uuid not in (select cashier_q_cust_uuid from cashier_queue) 
        #to filter the ones not in que
        #select count(*) from table

    def commence_simulation(self, time_open=850, closing_time=1300):
        """
        notes on threads 
        threads = [threading.Thread(target=func, args=[]) for func in funcs_to_run]
        for thread in threads:
            thread.start()
        """
        threads = []
        time_open = time_open
        while time_open < closing_time:
            time_open += 1
            next_cust = self.get_lowest_cust() #returns a dict
            
            if next_cust is not None and next_cust['customers_entry_time'] >= time_open: #if it's time for the customer to be in line
                #sulod sa q
                
                #lowest_cashier_uuid = self.get_least_loaded_cashier()[0][0] #get the lowest cashier
                self.que_customer(self.get_least_loaded_cashier()[0][0],next_cust['customer_uuid']) #put on the q of the lowest cashier
            working_cashiers = self.get_cashiers_that_have_people_in_line() #function name says it all
            #please continue here if u wanna sleep lol
            #but no
            print(working_cashiers)


if __name__ == "__main__":
    pass
            
                #thread.start()
                #do smth to join the threads
            #might need to populate threads for cashiers outside of the while loop and let them work instead of going through everyone while iterating.


                #self.cur.execute("""insert into cashier_queue (cashier_q_cashier_uuid, cashier_q_cust_uuid)""")
                

        #self.cur.execute("insert into cashier_queue (cashier_q_cashier_uuid, cashier_q_cust_uuid) VALUES ('{0}','{1}')".format( cashier_uuid, customer_uuid) )
        #self.db.commit() 
        #pasensya gid, kinanglan ko lg mag una anay subong.