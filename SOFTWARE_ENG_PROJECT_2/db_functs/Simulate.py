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

    def commence_simulation(self, time_open, closing_time):
        """
        notes on threads 
        threads = [threading.Thread(target=func, args=[]) for func in funcs_to_run]
        for thread in threads:
            thread.start()
        """
    
        while time_open <= closing_time:
            print(time_open)
            #diri ni sa dapat ma loop. nd mag loop sa time_open kada while

            next_cust = self.get_lowest_cust(time_open) 
            #gets all the customers thats equal or greater time open
            time_open += 1 


            if next_cust is not None: #if it's time for the customer to be in line
                #sulod sa q
                for next_cust_in_line in next_cust:

                    next_cust_time = next_cust_in_line[1]
                    #print(next_cust_time)
                    next_cust_uuid = next_cust_in_line[5]

                    if next_cust_time <= time_open:#double check cause im paranoid that way 
                #lowest_cashier_uuid = self.get_least_loaded_cashier()[0][0] #get the lowest cashier
                        self.que_customer(self.get_least_loaded_cashier()[0][0],next_cust_uuid) 
                #put on the q of the lowest cashier

            working_cashiers = self.get_cashiers_that_have_people_in_line() #function name says it all
            #please continue here if u wanna sleep lol
            #but no
            for cashier in working_cashiers:
                #print(cashier)
                self.cashier_work(cashier, time_open)
            #TODO THINGS. Now that you have the UUIDs of the CASHIERS, 
            """Grab the uuid and the entry time of the customer



            #working sql statement 
             select customers_entry_time, customer_uuid FROM customers WHERE customer_uuid in (select cashier_q_cust_uuid from cashier_queue where cashier_q_cashier_uuid='5c08aaf0-1687-429d-b551-33578e56cf5f');

             or 

            select customer_uuid FROM customers WHERE customer_uuid in (select cashier_q_cust_uuid from cashier_queue where cashier_q_cashier_uuid='5c08aaf0-1687-429d-b551-33578e56cf5f') ORDER BY customers_entry_time LIMIT 1; #grabs the last recent one ang una sa linya and start serving it
            """
           

if __name__ == "__main__":
    pass
            
                #thread.start()
                #do smth to join the threads
            #might need to populate threads for cashiers outside of the while loop and let them work instead of going through everyone while iterating.


                #self.cur.execute("""insert into cashier_queue (cashier_q_cashier_uuid, cashier_q_cust_uuid)""")
                

        #self.cur.execute("insert into cashier_queue (cashier_q_cashier_uuid, cashier_q_cust_uuid) VALUES ('{0}','{1}')".format( cashier_uuid, customer_uuid) )
        #self.db.commit() 
        #pasensya gid, kinanglan ko lg mag una anay subong.