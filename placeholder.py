from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from tkinter import scrolledtext

class EntPlaceHold(Entry):
    def __init__(self,master=None,placeholder='_PLACEHOLDER', color='gray',font = ('verdana', 8),justify="center"):
        super().__init__(master)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.font = font
        self.justify = justify
        self.default_fg_color = self['fg']

        self.bind('<FocusIn>',self.foc_in)
        self.bind('<FocusOut>',self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0,self.placeholder)
        self['fg'] = self.placeholder_color
        self['font'] = self.font
        self['justify'] = self.justify

    def foc_in(self,*args):
        if self['fg'] == self.placeholder_color:
            self.delete('0','end')
            self['fg'] = self.default_fg_color

    def foc_out(self,*args):
        if not self.get():
            self.put_placeholder()
