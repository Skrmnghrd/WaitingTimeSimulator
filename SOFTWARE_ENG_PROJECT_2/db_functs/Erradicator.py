#I can't breathe without putting starting the code on line 4 idky


class xErradicator:

    def __init__(self, cur):
        self.cur = cur

    def erradicate_everyone(self):
        """
        Things are beautiful because they have endings,
        We all die in the end ):)
        """
        #self.cur.execute("SHOW TABLES")
        
        tables = ['cashier_queue','customers', 'cashier']#self.cur.fetchall()

        for table in tables:
            self.cur.execute("delete from {0}".format(table))
        self.db.commit() 
        #pasensya gid, kinanglan ko lg mag una anay subong.
