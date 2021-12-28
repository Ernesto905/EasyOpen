import sqlite3
conn = sqlite3.connect('easyOpen.db')
c = conn.cursor()


#creates a new collection and addts to collection table 
#Then for every app in the list of apps, adds to the app table
def addNewCollection(collectionName, apps):
    c.execute("INSERT INTO Collections(name) VALUES (?);", (collectionName,))
    c.executemany(sql, seq_of_parameters) #FOR Apps



