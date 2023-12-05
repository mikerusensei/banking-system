import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from functions import greet
from view_profile import View_Profile_Window
from enroll_account import Enroll_Account_Window
from check_balance import Check_Balance_Window
from deposit_window import Deposit_Window
#from withdraw_window import Withdraw_Window
from widgetgenerator import LabelGeneratorPack, ButtonGeneratorPack

current_date = datetime.now()

class Login_Menu(tk.Toplevel):
    def __init__(self, customer_key, customer_value, master=None):
        super().__init__(master)
        self.view_profile_window = None
        self.enroll_account_window = None
        self.check_balance_window = None
        self.deposit_window = None
        self.withdraw_window = None
        self.customer_key = customer_key
        self.customer_value = customer_value
        self.__add_labels()
        self.__add_buttons()
        self.__configure_window()
        
    def __configure_window(self):
        self.title("Foobar's Bank")
        self.geometry("400x450")
        self.resizable(False, False)
        self.configure(bg="#C4FFF9")

        for widget in self.winfo_children():
            widget.config(font=("Calibri", 16))

    def __add_labels(self):
        label_configuration = [
            {"text": f"{current_date:%A, %B %d, %Y}\n", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"{greet()} {self.customer_value.get('username')}", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"What do you want to do today?\n\n", "anchor": "w", "bg": "#C4FFF9"},
        ]

        for config in label_configuration:
            LabelGeneratorPack(self)\
                .set_text(config["text"])\
                .set_anchor(config["anchor"])\
                .set_bg_color(config["bg"])\
                .build()

    def __add_buttons(self):
        button_configuration = [
            {"text": "View Profile", "command": self.show_view_profile_window, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Enroll Account", "command": self.show_enroll_account_window, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Check Balance", "command": self.show_check_balance_window, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Deposit", "command": self.show_deposit_window, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Withdraw", "command": self.show_withdraw_window, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Log Out", "command": self.command_logout, "anchor": "w", "width": 15, "bg": "#07BEB8"},
        ]

        for config in button_configuration:
            ButtonGeneratorPack(self)\
                .set_text(config["text"])\
                .set_command(config["command"])\
                .set_anchor(config["anchor"])\
                .set_width(config["width"])\
                .set_bg_color(config["bg"])\
                .build()
    
    def show_view_profile_window(self):
        if not self.view_profile_window:
            self.view_profile_window = View_Profile_Window(self, self.customer_key, self.customer_value)
        self.iconify()
        self.view_profile_window.lift()

    def show_enroll_account_window(self):
        if not self.enroll_account_window:
            self.enroll_account_window = Enroll_Account_Window(self, self.customer_key, self.customer_value)
        self.iconify()
        self.enroll_account_window.lift()

    def show_check_balance_window(self):
        isUserVerified = self.customer_value['verified']
        if isUserVerified == True:
            if not self.check_balance_window:
                self.check_balance_window = Check_Balance_Window(self, self.customer_key, self.customer_value)
            self.iconify()
            self.check_balance_window.lift()
        else:
            messagebox.showerror("Error", "You don't have an account enrolled!")

    def show_deposit_window(self):
        isUserVerified = self.customer_value['verified']
        if isUserVerified == True:
            if not self.deposit_window:
                self.deposit_window = Deposit_Window(self, self.customer_key, self.customer_value)
            self.iconify()
            self.deposit_window.lift()
        else:
            messagebox.showerror("Error", "You don't have an account enrolled!")

    def show_withdraw_window(self):
        isUserVerified = self.customer.get_isUserVerified()
        if isUserVerified == True:
            if not self.withdraw_window:
                self.withdraw_window = Withdraw_Window(self, self.customer)
            self.iconify()
            self.withdraw_window.lift()
        else:
            messagebox.showerror("Error", "You don't have an account enrolled!")
    
    def command_logout(self):
        self.master.deiconify()
        self.destroy()
