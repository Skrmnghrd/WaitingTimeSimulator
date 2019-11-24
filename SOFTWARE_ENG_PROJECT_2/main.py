import sys
import MySQLdb
#custom import paths
sys.path.insert(0, "db_functs")
sys.path.insert(0, "simulator")
#ignore the errors if you're using an IDE, it'll run juzzz fine :>
from main_db_functs__ import db_functions
from Simulate import xSimulate

db = MySQLdb.connect(host='localhost',
                    user='root',
                    password='talablasani',
                    db='software_project_two')
cur = db.cursor() 

x = db_functions(\
waiting_time=(2,5), 
cashiers=2, 
customers=5, 
time=(840,1200)
)
x.clear_database()
x.add_cashier()
x.add_customer()
cur = db.cursor()
y = xSimulate(cur)
y.commence_simulation()
#x.que_customer('b0365ac8-9ff0-40a0-8b90-faee5adebd4e', 'af5d9016-a913-442f-98eb-ca2e015b66fc')

"""cashier = 'ddc1f831-19ca-493e-b140-91980924460c'
customers = ['1c19947e-f3cb-4e48-b876-a8d09988b5f8','e502f26a-4b47-4e8e-819f-86ee917def23','150631f5-4113-419c-8bb0-86280f99a31c']

for things in customers:
    x.que_customer(cashier, things)

print(x.get_cashiers())
print(x.get_customers())"""


"""

WElcome to the trash bin

where our deepest thoughts 
and our arrid feelings lay down on a sea of sorrow





#sa generator na sa dapat mamangkot sang muni na args, tandai nga ang sa db funcs dapat function lg sa db ang hmuon ya, 
#sa generator, or redundant na ang generator? sa simulate ma dalagan ang increment sang time kag ang kuha kuha sang mga enteties, sooo. dira na lg guro mamangkot sa simulator,
#ah get's ko na, ang sa generator, dira sa ma for loop kng pila gid man kinanglan mo
#generate()
#simulate() and that's it
#get data
"""