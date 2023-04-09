import wget
from tkinter import *

def download():
    print('download')


def speed_one_twenty_five():
    print('speed1.25')


root = Tk()


def show_button():
    start_button = Button(root, height='80px', width='109px', command=lambda: launch_ver_one())


root.geometry('1000x600')
root.title("Song Spedup-er")

menu_zone = Frame(root, borderwidth=3, bg='white')
menu_zone.place(x=300, y=300)

file_menu = Menubutton(menu_zone, text='Vitesse', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
file_menu.grid(row=0,column=0)

speed_menu = Menu(file_menu)
speed_menu.add_command(label='Vitesse 1.25', command=speed_one_twenty_five)
file_menu.configure(menu=show_button())



root.mainloop()
