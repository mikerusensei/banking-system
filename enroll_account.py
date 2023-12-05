import tkinter as tk
from savingsaccount_window import SavingsAccount_Window
from checkingaccount_window import CheckingAccount_Window
from widgetgenerator import LabelGeneratorPack, ButtonGeneratorPack

class Enroll_Account_Window(tk.Toplevel):
    def __init__(self, master=None, customer_key=None, customer_value=None):
        super().__init__(master)
        self.customer_key = customer_key
        self.customer_value = customer_value
        self.__add_labels()
        self.__add_buttons()
        self.__configure_window()
        

    def __configure_window(self):
        self.title("Enroll Account")
        self.geometry("300x300")
        self.resizable(False, False)
        self.configure(bg="#C4FFF9")

        for widget in self.winfo_children():
            widget.config(font=("Calibri", 16))

    def __add_labels(self):
        label_configuration = [
            {"text": f"Type of Accounts\n", "anchor": "w", "bg": "#C4FFF9"},
        ]

        for config in label_configuration:
            LabelGeneratorPack(self)\
                .set_text(config["text"])\
                .set_anchor(config["anchor"])\
                .set_bg_color(config["bg"])\
                .build()
            
    def __add_buttons(self):
        button_configuration = [
            {"text": "Savings Account", "command": self.show_savingsaccount_window, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Checking Account", "command": self.show_checkingaccount_window, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Joint Account", "command": None, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Return", "command": self.command_return, "anchor": "w", "width": 15, "bg": "#07BEB8"},
        ]

        for config in button_configuration:
            ButtonGeneratorPack(self)\
                .set_text(config["text"])\
                .set_command(config["command"])\
                .set_anchor(config["anchor"])\
                .set_width(config["width"])\
                .set_bg_color(config["bg"])\
                .build()
    
    def show_savingsaccount_window(self):
        SavingsAccount_Window(self.master, self.customer_key, self.customer_value)
        self.destroy()
    
    def show_checkingaccount_window(self):
        CheckingAccount_Window(self.master, self.customer_key, self.customer_value)
        self.destroy()
    
    def show_jointaccount_window(self):
        pass

    def command_return(self):
        self.destroy()
        self.master.deiconify()

    def destroy(self):
        super().destroy()
        if self.master:
            self.master.enroll_account_window = None
