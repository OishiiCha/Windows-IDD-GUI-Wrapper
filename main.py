import os, ctypes, subprocess
from tkinter import *
from PIL import ImageTk, Image

add_screen = 'deviceinstaller64 enableidd 1'
remove_screen = 'deviceinstaller64 enableidd 0'
add_driver = 'deviceinstaller64 install usbmmidd.inf usbmmidd'
remove_driver = 'deviceinstaller64 stop usbmmidd || deviceinstaller64 remove usbmmid'
pro_local = os.getcwd()
driver_folder = '\\usbmmidd_v2'
driver_path = str(pro_local + driver_folder)
bfont = ('calibri', 12, 'bold')

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def run_command(command):
    os.system(str('cd ' + driver_path + '\\' + ' && ' + command))

def error_window():
    windowx = Tk()
    windowx.geometry('300x100')
    windowx.resizable(width=False, height=False)
    windowx.configure(bg='orange')
    windowx.title('Warning')
    windowx.eval('tk::PlaceWindow . center')
    windowx.iconbitmap('images/windowx.ico')
    wlabel = Label(windowx, text='Warning!\nThis application requires\nadmin privileges or password', bg='orange', font=('calibri', 15, 'bold'))
    wlabel.place(x=150, y=50, anchor='center')


root = Tk()
root.geometry('300x200')
root.resizable(width=False, height=False)
root.configure(bg='grey12')
root.title('Virtual Display')
root.eval('tk::PlaceWindow . center')
root.iconbitmap('images/root.ico')

width_i = 80
height_i = 80

add_d_i = Image.open("images/adddriver.png")
add_d_r = add_d_i.resize((width_i, height_i), Image.ANTIALIAS)
add_d_image = ImageTk.PhotoImage(add_d_r)

remove_d_i = Image.open("images/removedriver.png")
remove_d_r = remove_d_i.resize((width_i, height_i), Image.ANTIALIAS)
remove_d_image = ImageTk.PhotoImage(remove_d_r)

add_di_i = Image.open("images/addscreen.png")
add_di_r = add_di_i.resize((width_i, height_i), Image.ANTIALIAS)
add_di_image = ImageTk.PhotoImage(add_di_r)

remove_di_i = Image.open("images/removescreen.png")
remove_di_r = remove_di_i.resize((width_i, height_i), Image.ANTIALIAS)
remove_di_image = ImageTk.PhotoImage(remove_di_r)

add_driver_b = Button(root, image=add_d_image, font=bfont, borderwidth=0, highlightthickness=0, activebackground='grey12', bg='grey12', command=lambda:run_command(add_driver))
add_driver_b.place(x=80, y=60, anchor='center')
remove_driver_b = Button(root, image=remove_d_image, font=bfont, borderwidth=0, highlightthickness=0, activebackground='grey12', bg='grey12', command=lambda:run_command(remove_driver))
remove_driver_b.place(x=220, y=60, anchor='center')
add_screen_b = Button(root, image=add_di_image, font=bfont, borderwidth=0, highlightthickness=0, activebackground='grey12', bg='grey12', command=lambda:run_command(add_screen))
add_screen_b.place(x=80, y=140, anchor='center')
remove_screen_b = Button(root, image=remove_di_image, font=bfont, borderwidth=0, highlightthickness=0, activebackground='grey12', bg='grey12', command=lambda:run_command(remove_screen))
remove_screen_b.place(x=220, y=140, anchor='center')

if __name__ == '__main__':
    if not isAdmin():
        error_window()
    root.mainloop()