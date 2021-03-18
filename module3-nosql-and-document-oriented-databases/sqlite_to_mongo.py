# I do not think one was harder than the other. I had a harder time with
# this assignment (MongoDB) because of having to get information from
# various tables in a sqlite database, with the data not being the same
# amount from each table.
import sqlite3
import pymongo

collection_name = 'rpg_data'

def create_mdb_connection(collection_name):
    client = pymongo.MongoClient("mongodb://172.18.0.4/{}?retryWrites=true&w=majority".format(collection_name))
    return client


def create_sl_connection(extraction_db="rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(extraction_db)
    return sl_conn


def execute_query(curs, query):
    return curs.execute(query).fetchall()


query = """SELECT cc.name, level, exp, hp, strength, intelligence, dexterity, wisdom,
       GROUP_CONCAT(ai.name) as items,
       CASE
           WHEN aw.item_ptr_id is null THEN "None"
           ELSE GROUP_CONCAT(ai.name)
       END weapons
FROM charactercreator_character cc
LEFT OUTER JOIN charactercreator_character_inventory cci
    on cc.character_id = cci.character_id
LEFT JOIN armory_item ai
    on ai.item_id = cci.item_id
LEFT JOIN armory_weapon aw
    on cci.item_id = aw.item_ptr_id
GROUP BY cc.name"""



def insert_documents_from_sqlite(mongo_db, sl_curs, query):
    rows = execute_query(sl_curs, query)
    for row in rows:
        keys = ["name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom", "items", "weapons"]
        doc = {}
        for i,key in enumerate(keys):
            key_value = {key: row[i]}
            doc.update(key_value)
        mongo_db.insert_one(doc)


def show_all(collection):
    all_docs = list(collection.find())
    return all_docs
#

sl_conn = create_sl_connection()
sl_curs = sl_conn.cursor()
client = create_mdb_connection("rpg_data")
collection = client.rpg_data.rpg_data
collection.drop({})
insert_documents_from_sqlite(collection, sl_curs, query)


print(show_all(collection))
