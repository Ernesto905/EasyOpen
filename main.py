from fileHandler import MainWindow
import tkinter as tk
from sqliteStore import c

def main():
    #create databse
    initializeDatabase()
    
    #setup main window
    root = tk.Tk()
    root.title("Easy Open")
    
    #Run main window
    mainCall = MainWindow(root)
    root.mainloop()
    
def initializeDatabase():

    c.execute("PRAGMA foreign_keys = ON")
    c.execute("""CREATE TABLE IF NOT EXISTS Collections(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE
    )""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS Apps(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                path TEXT UNIQUE
    )""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS CollectionToApps(
                collection_id INT,
                app_id INT,
                PRIMARY KEY(collection_id, app_id) 
                FOREIGN KEY(collection_id) REFERENCES Collections(id)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY(app_id) REFERENCES Apps(id)
                    ON DELETE CASCADE ON UPDATE CASCADE
    )""")   

    c.execute("""CREATE TRIGGER IF NOT EXISTS delete_unused_tags
                AFTER DELETE ON Collections
                BEGIN
                    DELETE 
                    FROM Apps 
                    WHERE NOT EXISTS ( SELECT NULL
                                    FROM CollectionToApps
                                    WHERE Apps.id = CollectionToApps.app_id);
                END;
    """
    )
if __name__ == '__main__':
    main()

   
