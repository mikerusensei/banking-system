import tkinter as tk
from datetime import datetime
from functions import *
from widgetgenerator import LabelGeneratorPack, ButtonGeneratorPack
from create_account import Create_Account 
#from testapp import Create_Account
from login import Login

current_date = datetime.now()
current_tim = current_date.strftime("%I:%M %p")

class GUIBank(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_account_window = None
        self.login_window = None
        self.__add_label()
        self.__add_button()
        self.__config_window()
        self.run()

    def __config_window(self):
        self.title("Foobar's Bank")
        self.geometry("500x500")
        self.resizable(False, False)
        self.configure(bg="#C4FFF9")

        for widget in self.winfo_children():
            widget.config(font=("Calibri", 16))

    def __add_label(self):
        label_configuration = [
            {"text": f"{current_date:%A, %B %d, %Y}\n", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"\n\n{greet()}", "anchor": "w", "bg": "#C4FFF9"},
            {"text": "Welcome to FooBar's Bank\n\n\n", "anchor": "w", "bg": "#C4FFF9"},
            {"text": "\n\n\n[OPTIONS]", "anchor": "w", "bg": "#C4FFF9"},
        ]

        for config in label_configuration:
            LabelGeneratorPack(self)\
                .set_text(config["text"])\
                .set_anchor(config["anchor"])\
                .set_bg_color(config["bg"])\
                .build()
            
    def __add_button(self):
        button_configuration = [
            {"text": "Create Account", "command": self.create_account, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Log In", "command": self.login, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Exit", "command": self.destroy, "anchor": "w", "width": 15, "bg": "#07BEB8"},
        ]
        
        for config in button_configuration:
            ButtonGeneratorPack(self)\
                .set_text(config["text"])\
                .set_command(config["command"])\
                .set_anchor(config["anchor"])\
                .set_width(config["width"])\
                .set_bg_color(config["bg"])\
                .build()

    def create_account(self):
        if not self.create_account_window:
            self.create_account_window = Create_Account(self)
        self.iconify()
        self.create_account_window.lift()

    
    def login(self):
        if not self.login_window:
            self.login_window = Login(self)
        self.iconify()
        self.login_window.lift()
    

    def run(self):
        self.mainloop()
