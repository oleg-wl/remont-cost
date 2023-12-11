import pandas as pd
from sqlite3 import connect

def create_table():
    
    conn = connect('/home/oleg_vl/Projects/remont-cost/remont/db.sqlite3')
    df = pd.read_sql('SELECT * FROM form_purchases as p LEFT JOIN form_types as t ON p.types_id = t.id', conn)

    df.day = df.day.astype('datetime64[ns]')
    df.day = df.day.dt.strftime('%Y-%m')

    table = pd.pivot_table(df, index=[df.day, 'type_name'], values=['amount'], aggfunc='sum')
    tb = table.to_html()

    return tb
