from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog

import os

class nbDark(Frame):
    def __init__(self, main=None):
        Frame.__init__(self, main)
        
        self.parent = main
        
        self.winfo_toplevel().title("notepad")
        
        self.openbutton = Button(main, text='Open', command= lambda: opennew (self), width=6, bg='#191919',
                          fg='#FFF', background='#000', activebackground='#000', activeforeground='#FCF8E8', borderwidth=0, relief=SUNKEN)
        
        self.savebutton = Button(main, text='Save', command= lambda: savenew (self), width=6, bg ='#191919',
                          fg='#FFF', background='#000', activebackground='#000', activeforeground='#FCF8E8', borderwidth=0, relief=SUNKEN)
        

        self.separator = Frame(main, bg="#99aab5", height=1, bd=0)
        
        self.write = Text(main, bg='#000', height= 20, fg='#FFF', insertbackground='#99aab5', relief=FLAT, yscrollcommand='TRUE')
        
        self.GUI()
    
     
    def GUI(self):

            self.openbutton['font'] = 'Terminal', 8
            self.openbutton.grid(row=0, column = 0, sticky=NW)
            
            self.savebutton['font'] = 'Terminal', 8
            self.savebutton.grid(row=0, column = 1, sticky=NW)
            
            self.separator.grid(row=1, column=0, columnspan=2, ipadx=5000, pady=0, sticky=S)
        
            self.write['font'] = 'Tahoma', 11
            self.write.grid(row=2, column = 0, columnspan=4, sticky=N+S+W+E)
            
            return None
    
def opennew(self):
            file_name = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])                  
            with open(file_name, "r") as file:
                    if os.path.splitext(file_name)[1] == ".txt":
                        self.write.delete(0.0, END)
                        self.write.insert(0.0, file.read())
                        file.close()
                    return None
             
def savenew(self):
    savelocation = filedialog.asksaveasfile(mode='w', filetypes=[("Text Files", "*.txt")], defaultextension=".txt")
    if savelocation is None:
        return None
        
    savetext = str(self.write.get(0.0, END))
    savelocation.write(savetext)
    savelocation.close()

def main():
    root = Tk()
    gui = nbDark(root)
    print(font.families())
    print(font.names())
    gui.parent.geometry('852x480')
    gui.parent.grid_columnconfigure(1, weight=1)
    gui.parent.grid_columnconfigure(2, weight=1)
    gui.parent.grid_rowconfigure(1, weight=0)
    gui.parent.grid_rowconfigure(2, weight=1)
    gui.parent.configure(background = '#000000')
    gui.mainloop()
    
main()