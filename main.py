from fileHandler import *
from sqliteStore import *

def main():
    #create databse
    initializeDatabase()
    
    #setup main window
    root = tk.Tk()
    root.title("Easy Open")
    
    #Run main window
    mainCall = handler(root)
    root.mainloop()
    
def initializeDatabase():
    c.execute("""CREATE TABLE IF NOT EXISTS Collections(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT
    )""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS Apps(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                app_path TEXT
    )""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS Adjuncts(
                collection_id INTEGER,
                app_id INTEGER,
                PRIMARY KEY(collection_id, app_id)    
    )""")   

if __name__ == '__main__':
    main()

   
