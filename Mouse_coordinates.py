# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:24:51 2023

@author: Mihail
"""


import tkinter as tk

def update_entry(Entry, coord):
    Entry.delete(0, tk.END)
    Entry.insert(0, coord)
    Entry.select_range(0,tk.END)
    Entry.focus_set()

def calculate_data_coords():
    x1, x2, y1, y2 = x1_data.get(), x2_data.get(), y1_data.get(), y2_data.get()
    try:
        x1_dat, x2_dat, y1_dat, y2_dat = float(x1), float(x2), float(y1), float(y2)
        x1_pix, x2_pix, y1_pix, y2_pix = float(x1_pixel), float(x2_pixel), float(y1_pixel), float(y2_pixel)
        x_pix, y_pix = root.winfo_pointerxy()
        x_scale = (x2_dat - x1_dat) / (x2_pix - x1_pix)
        x_dat = x_scale*(x_pix - x1_pix) + x1_dat
        y_scale = (y2_dat - y1_dat) / (y2_pix - y1_pix)
        y_dat = y_scale*(y_pix - y1_pix) + y1_dat
        data_Label.config(text='{:.3f}, {:.3f}'.format(x_dat, y_dat))

    except:
        data_Label.config(text='{}, {}, {}, {}'.format(x1, x2, y1, y2))


def get_coords(event, coordinate='None'):
    global x1_pixel, x2_pixel, y1_pixel, y2_pixel
    if coordinate == 'x1':
        x1_pixel = str(root.winfo_pointerxy()[0])
        update_entry(x1_Entry, x1_pixel)
    elif coordinate == 'x2':
        x2_pixel = str(root.winfo_pointerxy()[0])
        update_entry(x2_Entry, x2_pixel)
    elif coordinate == 'y1':
        y1_pixel = str(root.winfo_pointerxy()[1])
        update_entry(y1_Entry, y1_pixel)
    elif coordinate == 'y2':
        y2_pixel = str(root.winfo_pointerxy()[1])
        update_entry(y2_Entry, y2_pixel)
    elif coordinate == 'None':
        x1_pixel, x2_pixel, y1_pixel, y2_pixel = 'x1', 'x2', 'y1', 'y2'
        update_entry(x1_Entry, x1_pixel)
        update_entry(x2_Entry, x2_pixel)
        update_entry(y1_Entry, y1_pixel)
        update_entry(y2_Entry, y2_pixel)
        root.focus_set()

def get_mouse_pos():
    pixel_Label.config(text='{}, {}'.format(*root.winfo_pointerxy()))
    calculate_data_coords()
    root.after(100, get_mouse_pos)

root = tk.Tk()
root.attributes('-topmost',True)
root.focus_force()
root.bind('<x>', lambda event: get_coords(event, coordinate='x1'))
root.bind('<Control-x>', lambda event: get_coords(event, coordinate='x2'))
root.bind('<z>', lambda event: get_coords(event, coordinate='y1'))
root.bind('<Control-z>', lambda event: get_coords(event, coordinate='y2'))
root.bind('<r>', lambda event: get_coords(event))
root.bind('<Return>', lambda event: root.focus_set())

x1_pixel, x2_pixel, y1_pixel, y2_pixel = 'x1', 'x2', 'y1', 'y2'
x1_data, x2_data, y1_data, y2_data = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()



pixel_Label = tk.Label(root, width=20)
pixel_Label.grid(row=0, column=0, columnspan=4)

x1_Entry = tk.Entry(root, width=5, textvariable=x1_data)
x1_Entry.grid(row=1, column=0)
x2_Entry = tk.Entry(root, width=5, textvariable=x2_data)
x2_Entry.grid(row=1, column=1)
y1_Entry = tk.Entry(root, width=5, textvariable=y1_data)
y1_Entry.grid(row=1, column=2)
y2_Entry = tk.Entry(root, width=5, textvariable=y2_data)
y2_Entry.grid(row=1, column=3)

data_Label = tk.Label(root, width=20)
data_Label.grid(row=2, column=0, columnspan=4)

get_coords(event=None)
get_mouse_pos()
root.mainloop()
