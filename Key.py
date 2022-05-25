import tkinter ##-Importation de la bibliotheque tkinter. #1
from tkinter import * #2

def Key(event):
    print(event.keysym)

version="1.0"
root = Tk() #-Définition de la fenêtre dans tkinte.
root.title('What KEY ?!') ##-Nom de la fenêtre.
root.resizable(True, True) ##-Bloque la dimension de la fenêtre.
root.bind_all("<Key>",Key)
root.mainloop() ##-Boucle principal.