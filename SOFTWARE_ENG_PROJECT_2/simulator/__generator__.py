import __db__functions__main
import random
import uuid

class Generator:
#This class generates customers or cashiers
    def __init__(self, customers, cashiers, time_open, time_closing):

        """
        Initialize the functions
        amount_of_customers = int
        amount_of_cashiers = int
        
        """
        
        self.customer_pool = []
        self.customers = int
        self.cashiers = int
        self.time_open = int #time in minutes ex: 8am is 480minutes
        self.time_closing = int #time in minutes 
        pass
        

    def generate_customer(self):
        """
        Generates a customer with random uuid, random time entry and random service minutes
        needed
        """
        customer_uuid = str(uuid.uuid4())
        customer_time_done = 0
        customer_time_entered = random.randint(self.time_open,self.time_closing)
        customer_service_needed = random.randint(2-5) #random var 2-5?
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



