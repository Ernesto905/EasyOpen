import os 
import tkinter as tk
from tkinter import filedialog


class handler:
    def __init__(self, master):
        super().__init__()
        self.apps = []
        
        canvas = tk.Canvas(master, height=700, width=700, bg="orange")
        canvas.pack()
        
        myFrame = tk.Frame(master, height=50, width=600, bg= "grey")
        testLab = tk.Label(myFrame, text="this is a test").pack()
        myFrame.pack()
        
        
        self.myButton2 = tk.Button(master, text="Add an app!", command= self.addApp)
        self.myButton2.pack(pady=20)
        
        
        
        self.myButton3 = tk.Button(master, text="show apps", command=self.showApps)
        self.myButton3.pack(pady=20)
        
    def addApp(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
        self.apps.append(filename)
        self.addAppToFrame(self, filename)
    
    def addAppToFrame(self, fname, y):
        print("this is filename: " +str(fname))
        print("this is y:" + y)
        
        label = tk.Label(myFrame, text="fdsfdssdf").pack()
        
        
        
    def showApps(self):
        print(self.apps)
        
    
    
    
        




