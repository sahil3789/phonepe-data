import pymysql
import pandas as pd
from config import DATABASE
from components.data import transform

def connect():
    return pymysql.connect(db=DATABASE["DB_NAME"], 
                           user=DATABASE["DB_USERNAME"],
                           passwd=DATABASE["DB_PASSWORD"], 
                           host=DATABASE["DB_HOST"],
                           port=DATABASE["DB_PORT"])

def table_exists(table):
    try:
        connection = connect()
        cursor=connection.cursor()
    except:
        return "failed to connect to databse"

    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall()
    exist_table=[]
    for table_item in tables:
        exist_table.append(table_item[0])

    if table in exist_table:
        return True
    else:
        return False    

def write(data, table):
    try:
        connection =  connect()
        cursor=connection.cursor()
    except:
        return "failed to connect to databse"

    var_types = transform.get_var_types(data)
    query = "CREATE TABLE %s (%s)"%(table, var_types)
    cursor.execute(query)

    data.rename(columns={'transaction-type':'transactiontype'}, inplace=True)
    columns = "`,`".join([str(i) for i in data.columns.tolist()])

    for i,row in data.iterrows():
        query = "INSERT INTO `%s` (`"% (table) +columns + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
        cursor.execute(query, tuple(row))
   
    connection.commit()
    connection.close()

def read(table):
    
    connection =  connect()
    cursor = connection.cursor()
    
    query = "SELECT * FROM `%s`"%(table)
    cursor.execute(query)

    datarow = []

    field_names = [i[0] for i in cursor.description]

    records = cursor.fetchall()

    for row in records:
        datarow.append(row)
        
    data = pd.DataFrame(datarow,columns=field_names)

    connection.close()
    return data
    

