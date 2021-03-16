import sqlite3
from queries import all_queries
import pandas as pd

conn = sqlite3.connect("rpg_db.sqlite3")
curs = conn.cursor()

result_dfs = []

for quer in all_queries:
    curs.execute(quer)
    result = curs.fetchall()
    result_as_df = pd.DataFrame(result)
    result_dfs.append(result_as_df)

print(result_dfs[0].head(), '\n')
print(result_dfs[1].head(), "\n", "0: cleric, 1: fighter, 2: mage, 3: necromancer, 4: thief", "\n" )

for num in range(2, 5):
    to_call = result_dfs[num]
    print(to_call.head(), '\n')

for num in range(5, 7):
    to_call = result_dfs[num]
    print(to_call.head(20), "\n")

for num in range(7, 9):
    to_call = result_dfs[num]
    print(to_call.head(), '\n')


