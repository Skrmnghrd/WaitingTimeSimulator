#I can't breathe without putting starting the code on line 4 idky

class xQueCustomers:

    def __init__(self, cur):
        self.cur = cur

    def load_customer(self, cashier_uuid, customer_uuid):
        """
        Starts to que the customer to the corresponding cashier
        """
        #print('hello')
        self.cur.execute("insert into cashier_queue (cashier_q_cashier_uuid, cashier_q_cust_uuid,cashier_q_service_needed ) VALUES ('{0}','{1}',(SELECT customer_service_needed FROM customers WHERE customer_uuid='{2}'))".format( cashier_uuid, customer_uuid, customer_uuid) )
        self.db.commit() 
        #pasensya gid, kinanglan ko lg mag una anay subong.
