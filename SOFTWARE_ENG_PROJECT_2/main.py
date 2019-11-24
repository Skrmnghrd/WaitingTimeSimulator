import sys

#custom import paths
sys.path.insert(0, "db_functs")
sys.path.insert(0, "simulator")

#ignore the errors if you're using an IDE, it'll run juzzz fine :>
from main_db_functs__ import db_functions


x = db_functions(\
waiting_time=(2,5), 
cashiers=2, 
customers=120, 
time=(840,1200)
)

#sa generator na sa dapat mamangkot sang muni na args, tandai nga ang sa db funcs dapat function lg sa db ang hmuon ya, 
#sa generator, or redundant na ang generator? sa simulate ma dalagan ang increment sang time kag ang kuha kuha sang mga enteties, sooo. dira na lg guro mamangkot sa simulator,
#ah get's ko na, ang sa generator, dira sa ma for loop kng pila gid man kinanglan mo
print(x.clear_database())
#generate()
#simulate() and that's it
#get data