import pyodbc
import app_config
import pandas as pd
from dbconn import querydbtopandas 

items_calificaciones = querydbtopandas("""select * from dba.log_items_encuestas""")

def load_data_json():
    items_calificaciones = querydbtopandas("""select * from dba.log_items_encuestas""")
    valor = len(items_calificaciones)
    return valor