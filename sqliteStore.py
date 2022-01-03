import sqlite3
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
    WHERE Collections.name = ? """, (collectionName, ))
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