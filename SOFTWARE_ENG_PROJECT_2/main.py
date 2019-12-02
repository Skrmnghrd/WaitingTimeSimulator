import sys
import MySQLdb
#custom import paths
sys.path.insert(0, "db_functs")
sys.path.insert(0, "simulator")
sys.path.insert(0, "visualizer")
#ignore the errors if you're using an IDE, it'll run juzzz fine :>
from main_db_functs__ import db_functions
from Simulate import xSimulate
from main_visualize import visualize

db = MySQLdb.connect(host='localhost',
                    user='root',
                    password='talablasani',
                    db='software_project_two')


cur = db.cursor() 

#quick and dirty solution for inputs
#its 4:30am and I need to sleep :>

#if u run this alone, it could work :>
if __name__ == "__main__":

    min_time = int(input("Please enter the oepning time in minutes: " ))
    max_time = int(input("Please enter the closing time in minutes: " ))
    time=(min_time, max_time)
    print("Waiting time:!")
    min_waiting_time = int(input("Please enter the MINIMUM waiting time: "))
    max_waiting_time = int(input("Please enter the MAXXXXIMUM waiting time: "))
    cashiers = int(input("Please enter number of cashiers: "))
    min_customers = int(input("Please enter minimum number of customers: "))
    max_customers = int(input("Please enter maximum number of customers: "))

    customers = (min_customers, max_customers)
    waiting_time = (min_waiting_time, max_waiting_time)

    csv_name = str(input("please enter csv name: "))
    dist_plot_name = str(input("Please enter the bar graphs name: "))
    x = db_functions(\
    waiting_time=waiting_time, 
    cashiers=cashiers, 
    customers=customers, 
    time=time
    ) #time will be converted into seconds for exact measurement 

    z = visualize()

    x.clear_database()
    x.clear_database()
    x.clear_database()
    x.add_cashier()
    x.add_customer()
    cur = db.cursor()
    y = xSimulate(cur)

    print('Simulating! Please wait!')
    y.commence_simulation(time[0], time[1])


    #print(x.fetch_table_columns("customers"))
    Dframe = z.sql_to_data_frame(x.get_customers(), x.fetch_table_columns("customers"))


    z.save_data_frame_to_csv(Dframe, csv_name)
    #print(Dframe['customers_waiting_time'].notnull())
    z.data_frame_to_distplot(Dframe, cashiers, dist_plot_name, customers, waiting_time)

