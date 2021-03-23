from tkinter import *
from tkinter import filedialog
import pandas
import os, sys
import cmath

def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)


def Instructions():
    newWindow = Toplevel(window) 
    newWindow.title("New Window") 
    newWindow.geometry("700x300") 

    f = open(resolver_ruta("Instructions.txt"), "r")
    texto = f.read()
  
    # A Label widget to show in toplevel 
    Label(newWindow,  text = texto, justify=LEFT).pack() 

def browseFiles():
    filename = filedialog.askopenfilename(  initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (("CSV files","*.csv"),))
      
    # Change label contents
    
    label_file_explorer.configure(text= filename, wraplength=300)
    label_file_explorer.pack()

def write_file(lis):

    directory = filedialog.askdirectory()
    location = str(directory) + '/sentences.txt'

    with open(location, 'w') as f:
        for item in lis:
            f.write("%s\n" % item)

def get_list(filepath, sentence):
    
    lis = list()
    if filepath == 'File':
        lis = "No file has been selected."
    else:
        table = pandas.read_csv(filepath)
        for i, value in enumerate(table[str(table.columns[0])]):
            for header in table:
                string = ""
                for n, word in enumerate(sentence):
                    replacement = word[1:]
                    if word[0] == "@":
                        print(replacement, table[replacement][i], type(table[replacement][i]))
                        if n == 0:
                            string += str(table[replacement][i]).capitalize()
                        else:
                            string += str(table[replacement][i])    
                        string += " "
                    else:
                        string += word + " "

            lis.append(string)

    mylist = Listbox(window, yscrollcommand = scrollbar.set )
    for line in lis:
        mylist.insert(END, line)
    mylist.pack(fill = BOTH )
    scrollbar.config( command = mylist.yview )

    button_instruction = Button(window, text = "Save Sentences in txt", command = lambda: write_file(lis))
    button_instruction.pack()

def readFile():
    filepath = label_file_explorer['text']
    sentence = frase.get().split()
    get_list(filepath, sentence)
                                                                                         
# Create the root window
window = Tk()

# scroll bar
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )

# Set window title
window.title('Massive Sentence Creator')
# Set window size
window.geometry("500x500")
#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window, text = "File",width = 100, height = 4, fg = "red")      
button_explore = Button(window, text = "Browse Files",command = browseFiles)
button_explore.pack()
button_instruction = Button(window, text = "Instructions", command = Instructions)
button_instruction.pack()

# Create phrase to concatenate

labPhrase = Label(window, text="Insert your phrase below")
labPhrase.pack()
frase = Entry(window, width=400, )
frase.pack()

read = Button(window, text = "Create Sentences", command = readFile)
read.pack()

# Let the window wait for any events
window.mainloop()