from fileHandler import *
from testWindow import * 


def main():
    #setup main window
    
    root = tk.Tk()
    root.title("Test title")

    mainCall = handler(root)
    root.mainloop()
    
    #test window
    #root = tk.Tk()
    #window1 = Window(root, "test title", "500x500", "This is a text msessage")
    #return None
    
    
    
    
if __name__ == '__main__':
    main()
    


   
    