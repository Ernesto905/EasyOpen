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
                collectionID INTEGER PRIMARY KEY ASC,
                name TEXT
    )""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS Apps(
                appID INTEGER PRIMARY KEY ASC,
                app_path TEXT
    )""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS Adjuncts(
                CID INTEGER REFERENCES Collections(collectionID),
                AID INTEGER REFERENCES Apps(appID)
    )""")

if __name__ == '__main__':
    main()

   
