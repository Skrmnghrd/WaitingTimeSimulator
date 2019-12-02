#I can't breathe without putting starting the code on line 4 idky

class xCloseTransaction:
    def __init__(self, cur):
        self.cur = cur

    def end_transaction(self, cashier_uuid, customer_uuid, current_time):
        """
        Closes the transaction once and for all
        
        #still has some errors depending on the data structure, please fix okay? eat breakfast, drink coffee, go to church, and fix!


        """

        #self.cur.execute("SELECT * FROM customers WHERE customer_uuid='{0}'".format(customer_uuid))
        #customer = self.cur.fetchone() #we only need one
        cashier_uuid = cashier_uuid[0]

        payload = """UPDATE customers SET customers_time_done={0}, customers_served_by='{1}', customer_service_needed=0 WHERE customer_uuid='{2}' """.format(current_time, str(cashier_uuid), str(customer_uuid) )
        #SELECT (customers_time_done - customers_entry_time) as total from `customers` where customer_uuid='c93b0111-0138-4487-bb60-59001f492a2f'
        self.cur.execute(payload) #ERRR OVER HERE
        self.db.commit()
        

        #I could change the db, but the deadline is really cloooose
        get_customer_entry_time_and_time_done  = """SELECT customers_entry_time, customers_time_done FROM customers where customer_uuid='{0}'""".format(str(customer_uuid))

        self.cur.execute(get_customer_entry_time_and_time_done)
        row = self.cur.fetchall()
        cust_entry_time = row[0][0] #((1233,)) # I need that [0][0] to xtract
        cust_time_done = row[0][1]
        #print(cust_entry_time)
        #print('pre total wait time ' + str(total_waiting_time))
        total_waiting_time = (cust_time_done - cust_entry_time)
        print('POST total wait time ' + str(total_waiting_time))
        x = """ UPDATE customers SET customers_waiting_time={0} where customer_uuid='{1}'""".format(total_waiting_time, str(customer_uuid)) #float err over here
        
        #print(customer_uuid)
        self.cur.execute(x)
        self.db.commit()
        payload = """delete from cashier_queue where cashier_q_cust_uuid='{0}' """.format(str(customer_uuid)) #delete the q since it's already done
        self.cur.execute(payload)
        self.db.commit()
        #pasensya gid, kinanglan ko lg mag una anay subong.
