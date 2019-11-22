import MySQLdb

class xAddCustomer:


    def __init__(self, db):
        self.cur = db.cursor()
    def runme(self):
        dicty = {
            'customers_entry_time': 800,
            'customers_time_done':  1,
            'customers_served_by': 0
        }
        #don't use dict keys since they're not sorted so you get random values lol
        self.cur.execute("insert into `customers` ({0},{1},{2}) VALUES ({3},{4},{5})".format( \
        'customers_entry_time',
        'customers_time_done',
        'customers_served_by', 
        dicty['customers_entry_time'],
        dicty['customers_time_done'],
        dicty['customers_served_by']   ) )
        #print('Imported "add customer"')
        self.db.commit()
#insert into 'customers' (customers_entry_time, customers_time_done, customers_served_by)