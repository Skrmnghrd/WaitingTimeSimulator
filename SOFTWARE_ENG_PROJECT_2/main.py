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
time=(28800,61200)
x = db_functions(\
waiting_time=(120,300), 
cashiers=5, 
customers=700, 
time=(28800,61200)
) #time will be converted into seconds for exact measurement 

z = visualize()
"""
x.clear_database()
x.clear_database()
x.clear_database()
x.add_cashier()
x.add_customer()
cur = db.cursor()
y = xSimulate(cur)


print('Simulating! Please wait!')
y.commence_simulation(time[0], time[1])
"""
#z.sql_to_data_frame(x.get_customers(), 
#print(x.fetch_table_columns("customers"))
Dframe = z.sql_to_data_frame(x.get_customers(), x.fetch_table_columns("customers"))
#z.save_data_frame_to_csv(Dframe, 'test.csv')
#print(Dframe['customers_waiting_time'].notnull())
z.data_frame_to_distplot(Dframe)

