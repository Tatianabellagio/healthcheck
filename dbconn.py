### IMPORTS ###
import pyodbc
import pandas as pd
import os 
import sqlanydb
### CONFIGS ###



### QUERYDB ###
def querydb(query):
    try:
        conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=192.168.1.173;PORT=2638;DATABASE=DW_SMG;UID=usr_dw;PWD=dwsmg15;ClientCharset=UTF-8;TDS_Version=auto')
        cursor = conn.cursor()
        result = cursor.execute(query)
        rows = result.fetchall()
        columns = cursor.description
    except Exception as err:
        print("El error del SQL es: %s" % str(err))
    finally:
        conn.close()
    return (columns,rows)

host_dw="192.168.1.173:2638"
user_dw="usr_dw"
passwd_dw="dwsmg15"
db_dw="DW_SMG"
driver_dw = "Adaptive Server Enterprise"


### QUERY TO PANDAS ###
def querydbtopandas(query):
    try:
        conn = sqlanydb.connect(uid = user_dw , pwd=passwd_dw, host=host_dw, dbn = db_dw, charset='utf8')
        df = pd.read_sql(query,conn)
    except Exception as err:
        print("El error del SQL es: %s" % str(err))
    finally:
        conn.close()
    return df