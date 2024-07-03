import tkinter as tk
from tkinter import ttk
from os import system as sys
import os.path


class Background:
    def __init__(self, master, color, sizex, sizey, x, y):
        self.bg = tk.Canvas(master=master, width=sizex, height=sizey, bg=color, highlightthickness=1, highlightbackground='white')
        self.bg.place(x=x, y=y)

def get_output(command):
       result = os.popen(command)
       output = result.read().strip()
       return output
    
#OS check
debian = False
if get_output('cat /etc/os-release | tail -n 2 | head -n 1') == 'ID_LIKE=debian':
    debian = True
    
def main():
    #checks if Executables dir is present
    if os.path.isdir('Executables') == True:
        pass
    else:
        sys('mkdir Executables')
    
    root = tk.Tk()
    root.title('rms')
    root.resizable(False, False)
    root.geometry('250x230')

    Background(root, '#3E3D53', 301, 301, -1, -1)#main bg
    Background(root, '#1e1d2d', 200, 100, 25, 30)#secondary bg

    #Entry box stuff
    pathtext = tk.StringVar()
    pathbox = tk.Entry(root, textvariable=pathtext, background='#d3d3d3', width=23, font='Terminus 12', highlightbackground='#27263a', )
    
    #idk why, but on debian the entry box goes out of the frame, so i have to resize it
    if debian:
        pathbox.config(width=21)
        pathbox.place(x=28, y=80)
    else:
        pathbox.place(x=30, y=80)

    tk.Label(root, text='Path to C file:', font='Helvetica 18', background='#1e1d2d', foreground='white').place(x=55, y=40)
    
    #button
    def buttonpress():
        if os.path.isfile('Executables/temp'):
            sys('rm Executables/temp')
        
        sys('gcc ' + pathtext.get() + ' -o Executables/temp')
        newterminal()
    button = tk.Button(root, text='RUN MY SHIT', font='Terminus 20', background='#1e1d2d', foreground='white', activebackground='#1e1d2d', activeforeground='white', relief='raised', command=buttonpress)
    if debian:
        button.place(x=30, y=150)
    else:
        button.place(x=35, y=150)

    root.mainloop()

def newterminal():
    xfce4terminal = False
    konsole = False
    kitty = False
    alacritty = False
    xterm = False
    override = False
    st = False
    pkgmanager = 'pacman -Q '
    awkline = '1'
    
    #distro check
    if debian:
        pkgmanager = 'dpkg-query --list '
        awkline = '2' 
    else:
        pass

    if get_output(pkgmanager + "| grep xfce4-terminal | awk '{print $" + awkline + "}' | head -n 1" ) == "xfce4-terminal":
        xfce4terminal = True
    if get_output(pkgmanager + "| grep konsole | awk '{print $" + awkline + "}' | head -n 1" ) == "konsole":
        konsole = True
    if get_output(pkgmanager + "| grep kitty | awk '{print $" + awkline + "}' | head -n 1" ) == "kitty":
        kitty = True
    if get_output(pkgmanager + "| grep alacritty | awk '{print $" + awkline + "}' | head -n 1" ) == "alacritty":
        alacritty = True
    if get_output(pkgmanager + "| grep st | awk '{print $" + awkline + "}' | head -n 1" ) == "st":
        st = True
    if get_output(pkgmanager + "| grep xterm | awk '{print $" + awkline + "}' | head -n 1" ) == "xterm":
        xterm = True
    
    with open('terminal-override.txt') as f:
        term = f.read()

    if term == "xfce4-terminal\n":
        override = True
        sys('xfce4-terminal --hold -e ./Executables/temp')
    if term == "konsole\n":
        override = True
        sys('konsole --noclose -e ./Executables/temp')
    if term == "alacritty\n":
        override = True
        sys('alacritty --hold -e ./Executables/temp')
    if term == "kitty\n":
        override = True
        sys('kitty --hold -e ./Executables/temp')
    if term == "st\n":
        override = True
        sys("st -e bash -c './Executables/temp /NY; read'")
    if term == "xterm\n":
        override = True
        sys('xterm -hold -e ./Executables/temp')
        
        
    if xfce4terminal:
        if override == False:
            sys('xfce4-terminal --hold -e ./Executables/temp')
    elif konsole:
        if override == False:
            sys('konsole --noclose -e ./Executables/temp')
    elif alacritty:
        if override == False:
            sys('alacritty --hold -e ./Executables/temp')
    elif kitty:
        if override == False:
            sys('kitty --hold -e ./Executables/temp')
    elif st:
        if override == False:
            sys("st -e bash -c './Executables/temp /NY; read'")
    elif xterm:
        if override == False:
            sys('xterm -hold -e ./Executables/temp')


if __name__ == '__main__':
    main()
