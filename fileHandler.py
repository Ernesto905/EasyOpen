import os 
import tkinter as tk
from tkinter import filedialog, StringVar
from sqliteStore import addNewCollection, delete_a_collection, returnAll, returnApps, returnAllCollections


class MainWindow:
    def __init__(self, master):
        self.apps = []
        self.testList = []
        self.master = master
        self.collVar = StringVar()
        
        self.canvas = tk.Canvas(self.master, height=700, width=700, bg="white")
        self.canvas.create_text(100, 50, text="Current Collections:", fill="black", font=('Constantia 15 bold'))   
        self.canvas.pack(expand=True)
        
        self.frame = tk.Frame(self.canvas, bg="white")
        self.frame.place(x=0,y=80,relheight=0.8,relwidth=1)
        
        self.label = tk.Label(self.frame, textvariable=self.collVar, bg='white')
        self.label.pack(pady=20)
        
        self.newCollectionButton = tk.Button(self.frame, text="Create/add to a collection", command = self.new_collection)
        self.newCollectionButton.pack(pady=5)

        self.newCollectionButton = tk.Button(self.frame, text="Delete a collection", command = self.delete_collection)
        self.newCollectionButton.pack(pady=5)

        #list constantly updating list of collections and their apps on the canvas 
        self.update()
    
    
    #To be implemented later; will return all the apps in a collection in list format
    def get_apps(self, collectionName):
        print(returnApps(collectionName))
    
    def update(self):  
        data = returnAllCollections()
        format = ''
        for collectionName in data:
            format += f"{collectionName}\n"         
        
        if format != '': self.collVar.set(format)
        self.master.after(1000, self.update)
        
    def openApps(self):
        for path in self.apps:
            os.startfile(path)  
    
    
    def new_collection(self):
        self.apps = []
        self.createCollection = tk.Toplevel(self.master)     
        self.app = NewCollection(self.createCollection, self.apps)    
        
    def delete_collection(self):
        self.eraseCollection = tk.Toplevel(self.master)
        self.app = DeleteCollection(self.eraseCollection)

class DeleteCollection:
    def __init__(self, master):
        self.master = master
        
        self.frame = tk.Frame(self.master, height=200, width=200, bg="Black")        
        self.frame.pack()
        
        self.label = tk.Label(self.frame, text="Please input the name of the collection you'd like to delete")
        self.label.pack()
        
        self.enterCollection = tk.Entry(self.frame)
        self.enterCollection.pack()
        
        self.saveAndExit = tk.Button(self.frame, text="Save and exit", command= self.deleteCollection)
        self.saveAndExit.pack(pady=5)
        
        
        
    def deleteCollection(self):
        collectionName = self.enterCollection.get()
        delete_a_collection(collectionName)
        self.master.destroy()
        
class NewCollection:
    def __init__(self, master, apps):
        self.master = master
        self.apps = apps
        
        self.frame = tk.Frame(self.master, height=200, width=200, bg="Black")        
        self.frame.pack()
        
        self.label = tk.Label(self.frame, text="Please input the name of the new collection\n or collection you'd like to add to")
        self.label.pack()
        
        self.enterCollection = tk.Entry(self.frame)
        self.enterCollection.pack()
        
        self.addAppButton = tk.Button(self.frame, text="Add an app!", command= self.addApp)
        self.addAppButton.pack(pady=5)
        
        self.saveAndExit = tk.Button(self.frame, text="Save and exit", command= self.storeCollection)
        self.saveAndExit.pack(pady=5)
        
    def addApp(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("all files", "*.*"),("executables", "*.exe")))
        self.apps.append(filename)        
        
    def storeCollection(self):
        collectionName = self.enterCollection.get()
        addNewCollection(collectionName, self.apps)
        self.master.destroy()
        
    
    
        




