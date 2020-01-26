
import tkinter 
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
#default window width and height
def newFile():
    global File
    root.title("Untitled-Notepad")
    File=NONE
    TextArea.delete(1.0,ENDs)
def OpenFile():
    global File
    File=askopenfilename(defaultextension=".txt",
                            filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if File=="":
        File=NONE
    else:
        root.title(os.path.basname(File) + " - Notepad")
        TextArea.delete(1.0,END)
        f=open(File,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def SaveFile():
    global File
    if File==NONE:
        File=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                            filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if File=="":
            File=None
        else:
            f=open(File,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basname(File) + " - Notepad")
    else:
        f=open(File,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def QuitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad by Namrata")


if __name__ == '__main__':
  #Basic tkinter setup
  root= Tk ()
  root.title("Untitled-Notepad")
  root.geometry("644x788")
 

  TextArea=Text(root,font="lucida 13")
  File=None
  TextArea.pack(expand=TRUE,fill=BOTH)

  MenuBar=Menu(root)
  FileMenu=Menu(MenuBar,tearoff=0)
  #to open new file
  FileMenu.add_command(label="New",command=newFile)
  #to open existing file
  FileMenu.add_command(label="Open",command=OpenFile)
  #to save the file
  FileMenu.add_command(label="Save",command=SaveFile)

  FileMenu.add_separator()
  # exit file
  FileMenu.add_command(label="Exit",command=QuitApp)
  MenuBar.add_cascade(label="File",menu=FileMenu)
  #FileMenu ends
  #EditMenu Starts
  #EditMenu end
  EditMenu=Menu(MenuBar,tearoff=0)
  #to give feature of Cut
  EditMenu.add_command(label="Cut",command=cut)
  EditMenu.add_command(label="Copy",command=copy)
  EditMenu.add_command(label="paste",command=paste)
  MenuBar.add_cascade(label="Edit",menu=EditMenu)

  #Hlp meu start
  HelpMenu=Menu(MenuBar,tearoff=0)
  HelpMenu.add_command(label="About Notepad",command=about)
  MenuBar.add_cascade(label="Help",menu=HelpMenu)

  # hlp menu ends
  root.config(menu=MenuBar)

  scroll=Scrollbar(TextArea)
  scroll.pack(side=RIGHT,fill=Y)
  scroll.config(command=TextArea.yview)
  TextArea.config(yscrollcommand=scroll.set)


  root.mainloop()