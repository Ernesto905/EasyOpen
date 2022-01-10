import sqlite3
from typing import Collection
conn = sqlite3.connect('easyOpen.db')
c = conn.cursor()


#Inserts into the collections and apps tables. Also updates adjunct table if required.
def addNewCollection(collectionName, apps):
    c.execute("INSERT OR IGNORE INTO Collections(name) VALUES(?)", (collectionName, ))
    c.execute("SELECT id FROM Collections WHERE name = ?", (collectionName, ))
    collectionId = c.fetchone()[0]

    for app in apps:
        c.execute("INSERT OR IGNORE INTO Apps(app_path) VALUES(?)", [app])
        c.execute("SELECT id FROM Apps WHERE app_path = ?", (app,))
        appId = c.fetchone()[0]
        c.execute("INSERT OR REPLACE INTO Adjuncts(collection_id, app_id) VALUES(?, ?)", (collectionId, appId))

    conn.commit()

#Returns all the paths associated with a collection name
def returnApps(collectionName):
    c.execute("""
    SELECT Apps.app_path
    FROM Apps
    INNER JOIN Adjuncts
        ON Apps.id = Adjuncts.app_id
    INNER JOIN Collections
        ON Collections.id = Adjuncts.collection_id
    WHERE Collections.name = ? 
    """, (collectionName, ))
    return c.fetchall()


#Returns all Collections as well as the paths associated with them 
def returnAll():
    c.execute("""
    SELECT Collections.name, Apps.app_path
    FROM Apps
    INNER JOIN Adjuncts
        ON Apps.id = Adjuncts.app_id
    INNER JOIN Collections
        ON Collections.id = Adjuncts.collection_id
    """)
    return c.fetchall()

#Return all the paths associated with a collection
def returnPaths(collectionName):
    c.execute("""
    SELECT Collections.name, Apps.app_path
    FROM Apps
    INNER JOIN Adjuncts
        ON Apps.id = Adjuncts.app_id
    INNER JOIN Collections
        ON Collections.id = Adjuncts.collection_id
    WHERE Collections.name = ?  
    """, (collectionName,))
    return c.fetchall()


#return a list of all collections
def returnAllCollections():

    conn.row_factory = lambda cursor, row: row[0] #when accessing single sqlite columns, will return values as list of strings rather than tuples
    c = conn.cursor()
    
    c.execute("SELECT ALL name FROM Collections")
    allCollections = c.fetchall()
    
    return allCollections