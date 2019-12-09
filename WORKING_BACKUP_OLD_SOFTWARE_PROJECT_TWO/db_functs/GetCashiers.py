#I can't breathe without putting starting the code on line 4 idky


class xGetCashiers:

    def __init__(self, cur):
        self.cur = cur

    def fetch_cashiers(self):
        self.cur.execute("SELECT * FROM cashier")
        return(self.cur.fetchall())