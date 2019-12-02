from flask import Flask, render_template, flash, url_for, request, send_from_directory, jsonify
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, BooleanField, IntegerField
from flask_wtf.file import FileField #needed for future upload needs
from flask_jsglue import JSGlue #DO YOU WANT JQUERY OR NOT?
from time import sleep
#client can just hit me up so I deploy this on herhis server

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


jsglue = JSGlue()
app = Flask(__name__)
jsglue.init_app(app)




class FORM_get_input(Form):
    min_time = IntegerField()
    max_time = IntegerField()

    min_wait_time = IntegerField()
    max_wait_time = IntegerField()

    cashiers = IntegerField("Cashier")

    customer_min = IntegerField("CustomerMin")
    customer_max = IntegerField("CustomerMax")
    
    csv_name = StringField()
    plot_name = StringField()



@app.route('/', methods=['GET', 'POST']) #index home
def index():
    #form = FORM_get_input(request.form)
    form = FORM_get_input()
    return render_template('index.html', form=form)


@app.route('/_test')
def test():
    try:
        waiting_time = (int(request.args.get('min_wait_time')), int(request.args.get('max_wait_time')))

        cashiers  = int(request.args.get('cashiers'))

        customers = (int(request.args.get('customer_min')), int(request.args.get('customer_max')))

        time = (int(request.args.get('min_time')), int(request.args.get('max_time')))
        
        csv_name = str(request.args.get('csv_name'))

        plot_name  = str(request.args.get('plot_name'))

        #return something for the func to populate the picture and download link for the csv
        
    except:
        return jsonify(response="PLEASE DEAL WITH THE INPUT FIELDS ACCORDINGLY:\
        THE ONLY STRING INPUTS ARE THE \
        CSV NAME AND THE GRAPH NAME\
        other than that, all are integers")

    x = db_functions(waiting_time=waiting_time, cashiers=cashiers, customers=customers, time=time)

    z = visualize()
    x.clear_database()
    x.add_cashier()
    x.add_customer()
    cur = db.cursor()
    y = xSimulate(cur)
    y.commence_simulation(time[0], time[1])

    Dframe = z.sql_to_data_frame(x.get_customers(), x.fetch_table_columns("customers"))

    z.save_data_frame_to_csv(Dframe, csv_name)

    
    z.data_frame_to_distplot(Dframe, cashiers, plot_name, customers, waiting_time)
    return jsonify(response='allgood')
    #return jsonify(graph=z.data_frame_to_distplot(Dframe, cashiers, plot_name, customers, waiting_time), csv='csv')

app.secret_key='thequickbrownfoxjumpedoverthelazydog'
if __name__ == "__main__":
    app.secret_key='thequickbrownfoxjumpedoverthelazydog'
    app.run(port=8000, host="0.0.0.0", debug=True)
