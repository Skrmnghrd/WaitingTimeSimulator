#I can't breathe without putting starting the code on line 4 idky

class xCloseTransaction:
    def __init__(self, cur):
        self.cur = cur

    def end_transaction(self, cashier_uuid, customer_uuid, current_time):
        """
        Closes the transaction once and for all
        """

        #self.cur.execute("SELECT * FROM customers WHERE customer_uuid='{0}'".format(customer_uuid))
        #customer = self.cur.fetchone() #we only need one
        
        payload = """UPDATE customers SET customers_time_done={0}, customers_served_by='{1}', customer_service_needed=0 WHERE customer_uuid='{2}'""".format(int(current_time), str(cashier_uuid), str(customer_uuid) )
        self.cur.execute(payload)
        self.db.commit()
        payload = """delete from cashier_queue where cashier_q_cust_uuid='{0}' """.format(str(customer_uuid)) #delete the q since it's already done
        self.cur.execute(payload)
        self.db.commit()
        print('Transaction closed')
        #pasensya gid, kinanglan ko lg mag una anay subong.
