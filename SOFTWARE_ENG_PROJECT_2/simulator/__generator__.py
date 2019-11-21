class Generator:
#This class generates customers or cashiers
    def __init__(self, customers, cashiers):

        """
        Initialize the functions
        customers = int
        cashiers = int
        
        """
        self.customer_pool = []
        pass
        

    def generate_customer(self):
        customer_uuid = None
        customer_time_done = None
        customer_time_entered = None
        customer_service_needed = None #random var 2-5?
        served_by = None #cashier uuid
        #customer_id = None #this is auto incremented in the database
        return [
        customer_uuid,
        customer_time_done,
        customer_time_entered,
        customer_service_needed,
        served_by
         ] #return this when you wanna generate customer

    def generate_cashier(self):
        pass



