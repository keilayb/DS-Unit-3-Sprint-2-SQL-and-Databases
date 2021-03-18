import os
import sqlite3
import psycopg2
import pandas as pd

pg_dbname = os.environ["PG_DBNAME"]
pg_user = os.environ["PG_USER"]
pg_password = os.environ["PG_PASSWORD"]
pg_host = os.environ["PG_HOST"]
pg_port = os.environ["PG_PORT"]

sql_conn = sqlite3.connect('titanic.sqlite3')
sql_curs = sql_conn.cursor()

pg_conn = psycopg2.connect(dbname=pg_dbname, user=pg_user, password=pg_password, host=pg_host, port=pg_port)
pg_curs = pg_conn.cursor()

titanic_df = pd.read_csv('titanic.csv')
titanic_df = titanic_df.rename(columns={"Siblings/Spouses Aboard": "Siblings_Spouses_Aboard",
                                  "Parents/Children Aboard": "Parents_Children_Aboard"})
titanic_df['Name'] = titanic_df['Name'].str.replace("'", " ")

titanic = titanic_df.to_sql("titanic", con=sql_conn, if_exists="replace")

rows = sql_curs.execute("""SELECT * FROM titanic""").fetchall()

try:
    pg_curs.execute("""DROP TABLE IF EXISTS titanic""")
    pg_curs.execute("""CREATE TABLE titanic
    (Passenger_id integer not null,
     Survived integer,
     Pclass integer,
     Name varchar(500),
     Sex varchar(10),
     Age float,
     Siblings_Spouses_Aboard integer,
     Parents_Children_Aboard integer,
     Fare float,
     primary key (Passenger_id))""")
    for row in rows:
        insert_row = """INSERT INTO %s VALUES %s""" % ("titanic", row)
        pg_curs.execute(insert_row)
    pg_conn.commit()
    print("Created titanic in pg")

except psycopg2.DatabaseError as e:
    print("Error: %s" % e)

pg_conn.close()
sql_conn.close()

print("All done")