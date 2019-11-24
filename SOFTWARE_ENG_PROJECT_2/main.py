import sys

#custom import paths
sys.path.insert(0, "db_functs")
sys.path.insert(0, "simulator")
#ignore the errors if you're using an IDE, it'll run juzzz fine :>
from main_db_functs__ import db_functions




x = db_functions(\
waiting_time=(2,5), 
cashiers=2, 
customers=10, 
time=(840,1200)
)


#x.que_customer('b0365ac8-9ff0-40a0-8b90-faee5adebd4e', 'af5d9016-a913-442f-98eb-ca2e015b66fc')
"""
cashier = 'd643f42e-739e-4f44-bbf5-f39a007b6025'
customers = ['24cacf30-2ae0-467c-8169-8ec80c0bfb3c','1ea87369-3f86-405a-bb67-f78cfbe2d101','27a8a3cb-57ab-47df-b6ad-3aedaab1e7df']

for things in customers:
    x.que_customer(cashier, things)
"""
print(x.get_lowest_cust())
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