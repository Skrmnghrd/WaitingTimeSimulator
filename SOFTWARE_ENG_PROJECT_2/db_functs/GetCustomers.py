#I can't breathe without putting starting the code on line 4 idky


class xGetCustomer:

    def __init__(self, cur):
        self.cur = cur

    def fetch_customers(self):
        self.cur.execute("SELECT * FROM CUSTOMERS ORDER BY customers_entry_time")
        return(self.cur.fetchall())