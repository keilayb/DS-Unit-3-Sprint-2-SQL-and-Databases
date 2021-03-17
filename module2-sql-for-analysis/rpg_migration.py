import os
import sqlite3
import psycopg2

pg_dbname = os.environ["PG_DBNAME"]
pg_user = os.environ["PG_USER"]
pg_password = os.environ["PG_PASSWORD"]
pg_host = os.environ["PG_HOST"]
pg_port = os.environ["PG_PORT"]
extraction_db = "rpg_db.sqlite3"

sql_conn = sqlite3.connect(extraction_db)
sql_curs = sql_conn.cursor()

pg_conn = psycopg2.connect(dbname=pg_dbname, user=pg_user, password=pg_password, host=pg_host, port=pg_port)
pg_curs = pg_conn.cursor()

sql_curs.execute(
    """SELECT name 
    FROM sqlite_master 
    WHERE type = 'table'
    AND name NOT LIKE 'django%'
    AND name NOT LIKE 'sqlite%'
    AND name NOT LIKE 'auth%'""")

table_results = sql_curs.fetchall()
table_names = []
for table in table_results:
    table_names.append(table[0])
table_names[4], table_names[2] = table_names[2], table_names[4]
table_names[3], table_names[7] = table_names[7], table_names[3]

for table in table_names:
    sql_curs.execute("""SELECT SQL 
    FROM sqlite_master
    WHERE type = 'table'
    AND tbl_name = '{}'
    AND name NOT LIKE 'django%'
    AND name NOT LIKE 'sqlite%'
    AND name NOT LIKE 'auth%'
    """.format(table))
    create = sql_curs.fetchone()[0]
    create = create.replace("integer NOT NULL PRIMARY KEY AUTOINCREMENT", "SERIAL PRIMARY KEY")
    create = create.replace("bool", "integer")
    sql_curs.execute("""SELECT name
    FROM PRAGMA_TABLE_INFO('%s');""" % table)
    col_names = sql_curs.execute("""SELECT * FROM %s""" % table)
    rows = sql_curs.fetchall()

    try:
        pg_curs.execute("DROP TABLE IF EXISTS %s CASCADE" % table)
        pg_curs.execute(create)
        for row in rows:
            insert_row = """INSERT INTO %s VALUES %s""" % (table, row)
            pg_curs.execute(insert_row)
        pg_conn.commit()
        print("Created", table)

    except psycopg2.DatabaseError as e:
        print("Error: %s" % e)
        break

pg_conn.close()
sql_conn.close()

print("Closed connections")
