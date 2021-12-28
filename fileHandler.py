import os 
import tkinter as tk
from tkinter import filedialog, StringVar
from jsonStore import addToJson, returnAllCollections


class handler:
    def __init__(self, master):
        #super().__init__()
        self.apps = []
        self.master = master
        self.var = StringVar()
        
        self.canvas = tk.Canvas(self.master, height=700, width=700, bg="white")
        self.canvas.create_text(100, 50, text="Current Collections:", fill="black", font=('Constantia 15 bold'))   
        self.canvas.pack(expand=True)
        
        self.frame = tk.Frame(self.canvas, bg="white")
        self.frame.place(x=0,y=80,relheight=0.8,relwidth=1)
        
        self.label = tk.Label(self.frame, textvariable=self.var, bg='white')
        self.label.pack()
        
        self.newCollectionButton = tk.Button(self.frame, text="Create a collection", command = self.newCollection)
        self.newCollectionButton.pack(pady=5)
        
        #This button prints the current apps to the terminal (FOR TESTING PURPOSES)
        self.testButton = tk.Button(self.frame, text="Test", command = self.check)
        self.testButton.pack(pady=5)
        
        self.update()
        
    def check(self):
        print(self.apps)
        
    def openApps(self):
        for path in self.apps:
            os.startfile(path)  
    
    
    def update(self):  
        data = returnAllCollections()
        format = ''
        for collectionName in data:
            format += f"Collection: {collectionName}\nApps:"         
        if format != '': self.var.set(format)
        self.master.after(1000, self.update)
    
    def newCollection(self):
        self.createCollection = tk.Toplevel(self.master)     
        self.app = newCollection(self.createCollection, self.apps)        
        
class newCollection():
    def __init__(self, master, apps):
        self.master = master
        self.apps = apps
        
        self.frame = tk.Frame(self.master, height=200, width=200, bg="Black")        
        self.frame.pack()
        
        self.label = tk.Label(self.frame, text="Please input the name of the New collection")
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
        addToJson(collectionName, self.apps)
        self.master.destroy()
        
    
    
        




