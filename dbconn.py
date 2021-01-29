### IMPORTS ###
import pyodbc
import pandas as pd
import os 

### CONFIGS ###

user=os.getenv("user1")
passwd=os.getenv("passwd1")

### QUERYDB ###
def querydb(query):
    try:
        conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=192.168.1.173;PORT=2638;DATABASE=DW_SMG;UID='+user+';PWD='+ passwd+';ClientCharset=UTF-8;TDS_Version=auto')
        cursor = conn.cursor()
        result = cursor.execute(query)
        rows = result.fetchall()
        columns = cursor.description
    except Exception as err:
        print("El error del SQL es: %s" % str(err))
    finally:
        conn.close()
    return (columns,rows)

### QUERY TO PANDAS ###
def querydbtopandas(query):
    try:    
        conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=192.168.1.173;PORT=2638;DATABASE=DW_SMG;UID='+user+';PWD='+ passwd+';ClientCharset=UTF-8;TDS_Version=auto')
        df = pd.read_sql(query,conn)
    except Exception as err:
        print("El error del SQL es: %s" % str(err))
    finally:
        conn.close()
    return df
