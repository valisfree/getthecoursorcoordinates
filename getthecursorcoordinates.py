#!/usr/bin/env python3 

# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Get the cursor coordinates
# Created:     23.12.2018
# Version:     0.2
# Copyright:   (c) 2018, Vale_Phtor, valisfree@yandex.ru
# Licence:     Apache License version 2.0
#-------------------------------------------------------------------------------

from tkinter import *
import pyautogui

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.geometry("450x250+100+100")
        self.master.minsize(350,200)
        self.master.title("Get the cursor coordinates")
        self.f_top = LabelFrame(self.master, text='Coordinates')
        self.l1 = Label(self.f_top, width=100, height=5, 
        text="Coordinates", bg='gray', font="Arial 18")
        self.update_label()
        self.text = Text(width=25, height=5, wrap=WORD)
        self.text.insert(1.0, 'Press the spacebar to save the coordinate value.')
        self.master.bind('<space>', self.save_coordinates)
        self.f_top.pack(fill=X, padx=5, pady=5)
        self.l1.pack(fill=X)
        self.text.pack(padx=5, pady=5)
        self.master.mainloop()
    def update_label(self):
        self.coordinates = pyautogui.position()
        self.coordinates = "x:" + str(self.coordinates[1]) + ' y:' + str(self.coordinates[0])
        self.l1.configure(text=self.coordinates)
        self.master.after(1, self.update_label)
    def save_coordinates(self, x):
        self.coordinates = pyautogui.position()
        self.coordinates = "x:" + str(self.coordinates[1]) + ' y:' + str(self.coordinates[0])
        self.text.delete(1.0, END)
        self.text.insert(1.0, self.coordinates)

if __name__ == "__main__":
    root = Tk()
    Interface(root)
