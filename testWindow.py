class Window:
    def __init__(self, root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        #self.Label(self.root, text=message).pack()
        self.root.mainloop()
        pass
    pass