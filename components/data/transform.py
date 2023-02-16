import pandas as pd

def uppercase_first(data, field):
    data[field] = data[field].str.title()
    data[field] = data[field].str.replace("-"," ")
    return data

def get_var_types(data):   
    s = ""
    for i in dict(data.dtypes):
        if dict(data.dtypes)[i] == "object":
            s+=" "+i+" "+"VARCHAR(255),"
        elif dict(data.dtypes)[i] == "int64":
            s+=" "+i+" "+"BIGINT,"
        elif dict(data.dtypes)[i]=="float64":
            s+=" "+i+" "+"FLOAT," 
    return s[1:len(s)-1]    

def merge(joins, drops):
    data = pd.DataFrame.from_records(joins[0])             
    metrics = pd.DataFrame.from_records(joins[1])
    data=data.join(metrics)
    data = data.drop([drops[0], drops[1]], axis=1)
    return data
