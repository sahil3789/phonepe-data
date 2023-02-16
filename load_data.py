import pandas as pd
import json 
import math
from components.data import transform
from components.model import db

pd.set_option('display.max_colwidth', None)

years = [2018, 2019, 2020, 2021, 2022]

def aggregate_transactions():

    if db.table_exists("aggregate_transactions") == False:

        path = "pulse/phonepedata/aggregated/transaction/country/india"
        tmp_data = []
        tmp_metrics = []

        for year in years:
            for q in range(1,5):
                with open(path+"/"+str(year)+"/"+str(q)+".json", 'r') as f:
                    data = json.load(f)
                    for item in data["data"]["transactionData"]:
                        item["year"],item["quarter"] = [year,q]
                        tmp_data.append(item)
                        tmp_metrics.append(item["paymentInstruments"][0])
       
        data = transform.merge([tmp_data, tmp_metrics],["paymentInstruments", "type"])
        data.columns = ["transaction_type","year","quarter","transactions_M","amount_cr"]
        db.write(data,"aggregate_transactions")
    else:
        return   

def map_transactions():

    if db.table_exists("map_transactions") == False:

        path = "pulse/phonepedata/map/transaction/hover/country/india/"
        tmp_data = []
        tmp_metrics = []
        for year in years:
            for q in range(1,5):
                with open(path+str(year)+"/"+str(q)+".json", 'r') as f:
                    data = json.load(f)
                    for item in data["data"]["hoverDataList"]:
                        item["year"], item["quarter"] = [year, q]
                        tmp_data.append(item)
                        tmp_metrics.append(item["metric"][0])
        
        data = transform.merge([tmp_data,tmp_metrics],["metric","type"])
        data.columns = ['state','year','quarter','transactions_M','amount_cr']
        data["transactions_M"] = data["transactions_M"]/math.pow(10,6)
        data["amount_cr"] = (data["amount_cr"]/math.pow(10,7)).round(3)
        data = transform.uppercase_first(data, "state")
        db.write(data,"map_transactions")
    else:
        return    

def aggregate_users():

    if db.table_exists("aggregate_users") == False:
        
        path = "pulse/phonepedata/aggregated/user/country/india/"
        tmp_data = []
        for year in years:
            for q in range(1,5):
                with open(path+str(year)+"/"+str(q)+".json", 'r') as f:
                    data = json.load(f)
                    if data["data"]["usersByDevice"] is not None:
                        for item in data["data"]["usersByDevice"]:
                            item["year"], item["quarter"] = [year,q]
                            tmp_data.append(item)
                            
        data = pd.DataFrame.from_records(tmp_data)
        data.columns = ['brand','transactions_M','percentage','year','quarter']
        data["transactions_M"] = data["transactions_M"]/math.pow(10,6)
        db.write(data,"aggregate_users")
    else:
        return    

def map_users():
    
    if db.table_exists("map_users") == False:
       
        path = "pulse/phonepedata/map/user/hover/country/india/"
        tmp_data = []
        for year in years:
            for q in range(1,5):
                with open(path+str(year)+"/"+str(q)+".json", 'r') as f:
                    data = json.load(f)
                    for item in data["data"]["hoverData"]:
                        tmp_data.append({"year":year,"q":q,"state":item, "users_registered":data["data"]["hoverData"][item]["registeredUsers"], "appOpens":data["data"]["hoverData"][item]["appOpens"]})
     
        data = pd.DataFrame.from_records(tmp_data)      
        data.columns = ["year","quarter","state", "users_registered_M","appOpens_M"]
        data["users_registered_M"] = data["users_registered_M"]/math.pow(10,6)
        data["appOpens_M"] = data["appOpens_M"]/math.pow(10,6)
       
        data = transform.uppercase_first(data,"state")
        db.write(data,"map_users")
    else:
        return

try:
    print("loading data into mysql...may take a while")
    aggregate_transactions()
    aggregate_users()
    map_transactions()
    map_users()
    print("data inserted into databse")    
except:
    print("failed to load data")    