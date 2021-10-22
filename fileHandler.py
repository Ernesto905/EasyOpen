import os 
import tkinter as tk
from tkinter import filedialog


class handler:
    def __init__(self, master):
        self.apps = []
        
        canvas = tk.Canvas(master, height=700, width=700, bg="orange")
        canvas.pack()
        
        myFrame = tk.Frame(master,  height=50, width=600)
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
        
        myFrame = tk.Frame(master,  height=50, width=600)
        myFrame.pack()
        
        label = tk.Label(self.myFrame, text=y, bg="gray").pack()
        
        
        
        
        
    def showApps(self):
        print(self.apps)
        
    
    
    
        




