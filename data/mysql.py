import pymysql
import pandas as pd
from config import DATABASE

def connect():
    return pymysql.connect(db=DATABASE["DB_NAME"], user=DATABASE["DB_USERNAME"], passwd=DATABASE["DB_PASSWORD"],
                           host=DATABASE["DB_HOST"],port=DATABASE["DB_PORT"])

def read(table_name):
    connection =  connect()
    cursor = connection.cursor()
    
    query = "SELECT * FROM `%s`"%(table_name)
    cursor.execute(query)

    datarow = []

    field_names = [column[0] for column in cursor.description]

    records = cursor.fetchall()
    
    for row in records:
        datarow.append(row)
        
    data = pd.DataFrame(datarow,columns=field_names)

    connection.close()
    return data
    

