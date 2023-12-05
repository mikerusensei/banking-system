import tkinter as tk
import datetime
from tkinter import messagebox
from widgetgenerator import LabelGeneratorGrid, ButtonGeneratorGrid, EntryGeneratorGrid
from customer import Customer
from bank import Bank
from command import MessageBoxAskQuestion, Save_CustomerData

class Create_Account(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.__customers = Bank.get_list_customers()
        self.today = datetime.date.today()
        self.current_year = self.today.year
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
            {"text": "[CREATE ACCOUNT]", "column": 0, "row": 0, "bg": "#C4FFF9"},

            {"text": "\n[PERSONAL INFORMATION]\n", "column": 0, "row": 1, "bg": "#C4FFF9"},
            {"text": "Full Name:", "column": 0, "row": 2, "bg": "#C4FFF9"},
            {"text": "Birthdate:", "column": 0, "row": 3, "bg": "#C4FFF9"},
            {"text": "Sex:", "column": 0, "row": 4, "bg": "#C4FFF9"},
            {"text": "Nationality:", "column": 0, "row": 5, "bg": "#C4FFF9"},
            {"text": "Cellphone Number:", "column": 0, "row": 6, "bg": "#C4FFF9"},
            {"text": "Email Address:", "column": 0, "row": 7, "bg": "#C4FFF9"},

            {"text": "\n[ADDRESS INFORMATION]\n", "column": 2, "row": 1, "bg": "#C4FFF9"},
            {"text": "House Number:", "column": 2, "row": 2, "bg": "#C4FFF9"},
            {"text": "Street:", "column": 2, "row": 3, "bg": "#C4FFF9"},
            {"text": "Subdivision:", "column": 2, "row": 4, "bg": "#C4FFF9"},
            {"text": "Barangay:", "column": 2, "row": 5, "bg": "#C4FFF9"},
            {"text": "Municipality:", "column": 2, "row": 6, "bg": "#C4FFF9"},
            {"text": "Province", "column": 2, "row": 7, "bg": "#C4FFF9"},

            {"text": "\n[ACCOUNT INFORMATION]\n", "column": 0, "row": 8, "bg": "#C4FFF9"},
            {"text": "Preffered Username:", "column": 0, "row": 9, "bg": "#C4FFF9"},
            {"text": "Preffered Password:", "column": 0, "row": 10, "bg": "#C4FFF9"}
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
            {"column": 1, "row": 2, "variable": "fullname"},
            {"column": 1, "row": 3, "variable": "birthdate"},
            {"column": 1, "row": 4, "variable": "sex"},
            {"column": 1, "row": 5, "variable": "nationality"},
            {"column": 1, "row": 6, "variable": "cpnumber"},
            {"column": 1, "row": 7, "variable": "emailaddress"},

            {"column": 3, "row": 2, "variable": "housenum"},
            {"column": 3, "row": 3, "variable": "street"},
            {"column": 3, "row": 4, "variable": "subdivision"},
            {"column": 3, "row": 5, "variable": "barangay"},
            {"column": 3, "row": 6, "variable": "municipality"},
            {"column": 3, "row": 7, "variable": "province"},

            {"column": 1, "row": 9, "variable": "username"},
            {"column": 1, "row": 10, "variable": "password"}
        ]

        for config in entry_configuration:
            entry = EntryGeneratorGrid(self)\
                .set_pos(config["row"], config["column"])\
                .build()
            
            self.entries[config["variable"]] = entry

    def __add_button(self):
        button_configuration = [
            {"text": "Save", "command": self.command_save, "row": 11, "column": 3, "width": 15, "bg": "#07BEB8"},
            {"text": "Cancel", "command": self.command_cancel, "row": 11, "column": 2, "width": 15, "bg": "#07BEB8"},
        ]
        
        for config in button_configuration:
            ButtonGeneratorGrid(self)\
                .set_text(config["text"])\
                .set_command(config["command"])\
                .set_pos(config["row"], config["column"])\
                .set_width(config["width"])\
                .set_bg_color(config["bg"])\
                .build()

    def get_inputs(self):
        __id = f"{self.current_year}-0{len(self.__customers) + 1}"
        __fullname = self.entries["fullname"].get()
        __birthdate = self.entries["birthdate"].get()
        __sex = self.entries["sex"].get()
        __nationality = self.entries["nationality"].get()
        __cpnumber = self.entries["cpnumber"].get()
        __emailaddress = self.entries["emailaddress"].get()

        __housenumber = self.entries["housenum"].get()
        __street = self.entries["street"].get()
        __subdivision = self.entries["subdivision"].get()
        __barangay = self.entries["barangay"].get()
        __municipality = self.entries["municipality"].get()
        __province = self.entries["province"].get()
        __fulladdress = f"{__housenumber}, {__street}, {__subdivision}, {__barangay}, {__municipality}, {__province}"

        __username = self.entries["username"].get()
        __password = self.entries["password"].get()

        customer = Customer(__id, __fullname, __fulladdress, __birthdate, __sex, __nationality,
                                __cpnumber, __emailaddress, __username, __password)
        return customer

    def command_save(self):
        result_instance = MessageBoxAskQuestion("Do you want to proceed?")
        result = result_instance()
        if result == "yes":
            new_customer = self.get_inputs()
            new_customer_dictionary = new_customer.convert_to_dictionary()
            self.__customers.update(new_customer_dictionary)
            save = Save_CustomerData(self.__customers)
            save()
            self.master.deiconify()
            self.destroy()

    def command_cancel(self):
        self.destroy()
        self.master.deiconify()

    def destroy(self):
        super().destroy()
        if self.master:
            self.master.create_account_window = None
