import tkinter as tk
from tkinter import ttk
from os import system as sys
import os.path
from multiprocessing import Process

class Background:
    def __init__(self, master, color, sizex, sizey, x, y):
        self.bg = tk.Canvas(master=master, width=sizex, height=sizey, bg=color, highlightthickness=1, highlightbackground='white')
        self.bg.place(x=x, y=y)

def main():
    if os.path.isdir('Executables') == True:
        pass
    else:
        sys('mkdir Executables')
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry('250x230')

    Background(root, '#3E3D53', 301, 301, -1, -1)#main bg
    Background(root, '#1e1d2d', 200, 100, 25, 30)#secondary bg

    #Entry box stuff
    pathtext = tk.StringVar()
    pathbox = tk.Entry(root, textvariable=pathtext, background='#d3d3d3', width=23, font='Terminus 12', highlightbackground='#27263a')
    pathbox.place(x=30, y=80)

    tk.Label(root, text='Path to C file:', font='Helvetica 18', background='#1e1d2d', foreground='white').place(x=55, y=40)
    
    #button
    def buttonpress():
        if os.path.isfile('Executables/temp'):
            sys('rm Executables/temp')
        
        sys('gcc ' + pathtext.get() + ' -o Executables/temp')
        newterminal()

    tk.Button(root, text='RUN MY SHIT', font='Terminus 20', background='#1e1d2d', foreground='white', activebackground='#1e1d2d', activeforeground='white', relief='raised', command=buttonpress).place(x=35, y=150)

    root.mainloop()

def newterminal():
    def get_output(command):
            result = os.popen(command)
            output = result.read().strip()
            return output


    xfce4terminal = False
    konsole = False

    if get_output("pacman -Q | grep xfce4-terminal | awk '{print $1}'" ) == "xfce4-terminal":
        xfce4terminal = True
    elif get_output("pacman -Q | grep konsole | awk '{print $1}'") != "":
        konsole = True

    if xfce4terminal == True:
        sys('xfce4-terminal --hold -e ./Executables/temp')
    elif konsole == True:
        sys('konsole --noclose -e ./Executables/temp')


if __name__ == '__main__':
    main()