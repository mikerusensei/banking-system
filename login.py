import tkinter as tk
from tkinter import messagebox
from widgetgenerator import LabelGeneratorGrid, EntryGeneratorGrid, ButtonGeneratorGrid
from bank import Bank
from login_menu import Login_Menu

class Login(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.__customers = Bank.get_list_customers()
        self.__add_label()
        self.__add_entry()
        self.__add_button()
        self.__configure_window()

    def __configure_window(self):
        self.title("Foobar's Bank")
        self.resizable(False, False)
        self.configure(bg="#C4FFF9")

        for widget in self.winfo_children():
            widget.config(font=("Calibri", 16))

    def __add_label(self):
        label_configuration = [
            {"text": "[LOGIN]\n", "column": 0, "row": 0, "bg": "#C4FFF9"},

            {"text": "Username:", "column": 0, "row": 1, "bg": "#C4FFF9"},
            {"text": "Password:", "column": 0, "row": 2, "bg": "#C4FFF9"},
        ]

        for config in label_configuration:
            LabelGeneratorGrid(self)\
                .set_text(config["text"])\
                .set_pos(config["row"], config["column"])\
                .set_bg_color(config["bg"])\
                .build()
            
    def __add_entry(self):
        self.entries = {}

        entry_configuration = [
            {"column": 1, "row": 1, "variable": "username"},
            {"column": 1, "row": 2, "variable": "password"},
        ]

        for config in entry_configuration:
            entry = EntryGeneratorGrid(self)\
                .set_pos(config["row"], config["column"])\
                .build()
            
            self.entries[config["variable"]] = entry

    def __add_button(self):
        button_configuration = [
            {"text": "Cancel", "command": self.command_cancel, "column": 0, "row": 3, "width": 15, "bg": "#07BEB8"},
            {"text": "Login", "command": self.command_login, "column": 1, "row": 3, "width": 15, "bg": "#07BEB8"},
        ]
        
        for config in button_configuration:
            ButtonGeneratorGrid(self)\
                .set_text(config["text"])\
                .set_command(config["command"])\
                .set_pos(config["row"], config["column"])\
                .set_width(config["width"])\
                .set_bg_color(config["bg"])\
                .build()
            
    def command_login(self):
        __inputted_username = self.entries["username"].get()
        __inputted_password = self.entries["password"].get()

        for key, value in self.__customers.items():
            if value.get("username") == __inputted_username and value.get("password") == __inputted_password:
                __customer_value = value
                __customer_key = key
                Login_Menu(__customer_key, __customer_value, master=self.master)
                self.destroy()
                break
        else:
            messagebox.showerror("Error", "Wrong Username or Password!")


        '''for customer in self.__customers:
            customer_username = customer['username']
            customer_password = customer['password']
            if customer_username == __inputted_username and customer_password == __inputted_password:
                Login_Menu(customer, master=self.master)
                self.destroy()
                break
        else:
            messagebox.showerror("Error", "Wrong Username or Password!")   
        '''

    def command_cancel(self):
        self.destroy()
        self.master.deiconify()

    def destroy(self):
        super().destroy()
        if self.master:
            self.master.login_window = None
