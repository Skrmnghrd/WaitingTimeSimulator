#I can't breathe without putting starting the code on line 4 idky
import uuid

class xAddCashier:
    def __init__(self, cur):
        self.cur = cur

    def generate_cashier(self):
        payload = """
        INSERT INTO `cashier` (cashier_uuid, cashier_people_served)
        VALUES ('{0}', 0)
        """.format(str(uuid.uuid4()))
        self.cur.execute(payload)

        #print('Imported "add customer"')
        self.db.commit() #ignore the error since it'll run (main db functs is using this to put stuff in the db)


