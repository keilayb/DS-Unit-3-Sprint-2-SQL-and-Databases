import os
import psycopg2
from titanic_queries import all_queries

pg_dbname = os.environ["PG_DBNAME"]
pg_user = os.environ["PG_USER"]
pg_password = os.environ["PG_PASSWORD"]
pg_host = os.environ["PG_HOST"]
pg_port = os.environ["PG_PORT"]

pg_conn = psycopg2.connect(dbname=pg_dbname, user=pg_user, password=pg_password, host=pg_host, port=pg_port)
pg_curs = pg_conn.cursor()

results = []

for query in all_queries:
    pg_curs.execute(query)
    raw_result = pg_curs.fetchall()
    result = raw_result[0][0]
    results.append(result)

# Print statements for the results
print("Passengers that survived:", results[0])
print("Passengers that didn't survive:", results[1], "\n")

print("Passengers in 1st class:", results[2])
print("Passengers in 2nd class:", results[3])
print("Passengers in 3rd class:", results[4], "\n")

print("1st class passengers that survived:", results[5])
print("1st class passengers that didn't survive:", results[6])
print("2nd class passengers that survived:", results[7])
print("2nd class passengers that didn't survive:", results[8])
print("3rd class passengers that survived:", results[9])
print("3rd class passengers that didn't survive:", results[10], "\n")

print("Average age of survivors:", round(results[11]))
print("Average age of non-survivors:", round(results[12]), "\n")

print("Average age of 1st class passengers:", round(results[13]))
print("Average age of 2nd class passengers:", round(results[14]))
print("Average age of 3rd class passengers:", round(results[15]), "\n")

print("Average 1st class fare:", "$", round(results[16], 2))
print("Average 2nd class fare:", "$", round(results[17], 2))
print("Average 3rd class fare:", "$", round(results[18], 2), "\n")

print("Average fare of survivor:", "$", round(results[19], 2))
print("Average fare of non-survivor:", "$", round(results[20], 2), "\n")

print("Average siblings/spouses aboard 1st class:", round(results[21], 2))
print("Average siblings/spouses aboard 2nd class:", round(results[22], 2))
print("Average siblings/spouses aboard 3rd class:", round(results[23], 2), "\n")

print("Average siblings/spouses aboard for survivors:", round(results[24], 2))
print("Average siblings/spouses aboard for non-survivors", round(results[25], 2), "\n")

print("Average parent/children aboard 1st class:", round(results[26], 2))
print("Average parent/children aboard 2nd class:", round(results[27], 2))
print("Average parent/children aboard 3rd class:", round(results[28], 2), "\n")

print("Average parent/children aboard for survivors:", round(results[29], 2))
print("Average parent/children aboard for non-survivors:", round(results[30], 2), "\n")

print("No passengers have the same name.")