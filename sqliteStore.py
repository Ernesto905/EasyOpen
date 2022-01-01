import sqlite3
conn = sqlite3.connect('easyOpen.db')
c = conn.cursor()


#creates a new collection and addts to collection table 
#Then for every app in the list of apps, adds to the app table
def addNewCollection(collectionName, apps):
    c.execute("INSERT INTO Collections(name) VALUES(?)", [collectionName])
    lastCollectionID = c.lastrowid

    for app in apps:
        #Insert each new app into our app table and then join it's newly created id with the recently created collection id within the adjunct table
        c.execute("INSERT INTO Apps(app_path) VALUES(?)", [app])
        lastAppID = c.lastrowid
        c.execute("INSERT INTO Adjuncts(collection_id, app_id) VALUES(?, ?)", (lastCollectionID, lastAppID))

    

    conn.commit()