### IMPORTS ###
import pyodbc
import pandas as pd
import os 
import sqlanydb
### CONFIGS ###



### QUERYDB ###
def querydb(query):
    try:
        conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=;PORT=;DATABASE=D;UID=;PWD=;ClientCharset=UTF-8;TDS_Version=auto')
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
        conn = sqlanydb.connect(uid = user_dw , pwd=, host=, dbn = db_dw, charset='utf8')
        df = pd.read_sql(query,conn)
    except Exception as err:
        print("El error del SQL es: %s" % str(err))
    finally:
        conn.close()
    return df
