import pandas as pd #is this cheating? :> https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
import seaborn as sns 
import matplotlib.pyplot as plt

class visualize():
    def __init__(self):
        print('Visualize inititalized without error')

    def sql_to_data_frame(self, fetched_sql_data, sql_data_columns):
        """
        Fucntion does what is says :?
        """
        #fetched sql data is a tuple 
        
        listy = [x for x in fetched_sql_data]
        df = pd.DataFrame(listy)
        df.columns=sql_data_columns
        return(df)
    def save_data_frame_to_csv(self, dataframe, filename):
        df = dataframe
        df.to_csv(filename, index=None)
        print('saved')
        #would need to get the columns dynamically but here's a fixed one for now 
        #describe table, and shove it up columns
    def data_frame_to_distplot(self, dataframe, num_of_cashiers):
        
        plt.rcParams["patch.force_edgecolor"] = True
        customer_waiting_time = [(int(x) ) for x in dataframe['customers_waiting_time'].dropna() ]
        sns.set_style("dark")
        sns.set(color_codes=True)
        #customer_waiting_time = ( dataframe['customers_waiting_time'].dropna() * 60)
        customer_customer_service_needed = dataframe['customer_service_needed']
        customer_served_by = dataframe['customers_served_by']
        #print(customer_waiting_time)
        waiting_time_count = dataframe['customers_waiting_time'].dropna().value_counts()
        sns.distplot(customer_waiting_time, bins=20, kde=False, hist_kws=dict(edgecolor="k", linewidth=1.5) )
        #Dr Bob, please teach me more math T_T
        #https://github.com/mwaskom/seaborn/issues/479 don't use kde unless the cust is data savyyyy or is a bad ass in stat
        #plt.ylim(0, len(customer_waiting_time)) #bad idea
        #plt.ylim(waiting_time_count.min(), waiting_time_count.max())
        plt.xlabel('Customer Waiting Time in Minutes')
        plt.ylabel('Number of Customers')
        plt.title("Waiting Time with {} Number of Cashiers".format(num_of_cashiers))
        plt.savefig('Distplot.png')
        plt.show()