import tkinter as tk
from command import Save_CustomerData
from widgetgenerator import LabelGeneratorGrid, ButtonGeneratorGrid, EntryGeneratorGrid

class Profile_Update(tk.Toplevel):
    def __init__(self, master=None, customer_key=None, customer_value=None):
        super().__init__(master)
        self.customer_key = customer_key
        self.customer_value = customer_value
        self.__add_label()
        self.__add_button()
        self.__add_entry()
        self.__configure_window()

    def __configure_window(self):
        self.title("Update Profile")
        self.resizable(False, False)
        self.configure(bg="#C4FFF9")

        for widget in self.winfo_children():
            widget.config(font=("Calibri", 16))

    def __add_label(self):
        label_configuration = [
            {"text": "[UPDATE PROFILE]", "column": 0, "row": 0, "bg": "#C4FFF9"},

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
            {"text": "Save", "command": self.command_submit, "row": 11, "column": 3, "width": 15, "bg": "#07BEB8"},
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
        self.__fullname = self.entries["fullname"].get()
        self.__birthdate = self.entries["birthdate"].get()
        self.__sex = self.entries["sex"].get()
        self.__nationality = self.entries["nationality"].get()
        self.__cpnumber = self.entries["cpnumber"].get()
        self.__emailaddress = self.entries["emailaddress"].get()

        self.__housenumber = self.entries["housenum"].get()
        self.__street = self.entries["street"].get()
        self.__subdivision = self.entries["subdivision"].get()
        self.__barangay = self.entries["barangay"].get()
        self.__municipality = self.entries["municipality"].get()
        self.__province = self.entries["province"].get()
        self.__fulladdress = f"{self.__housenumber}, {self.__street}, {self.__subdivision}, {self.__barangay}, {self.__municipality}, {self.__province}"

        self.__username = self.entries["username"].get()
        self.__password = self.entries["password"].get()

    def command_submit(self):
        self.get_inputs()

        self.customer_value["name"] = self.__fullname
        self.customer_value["address"] = self.__fulladdress
        self.customer_value["birthdate"] = self.__birthdate
        self.customer_value["gender"] = self.__sex
        self.customer_value["nationality"] = self.__nationality
        self.customer_value["cpnumber"] = self.__cpnumber
        self.customer_value["emailaddress"] = self.__emailaddress
        self.customer_value["username"] = self.__username
        self.customer_value["password"] = self.__password
        
        save_data = Save_CustomerData({self.customer_key: self.customer_value})
        save_data.execute()

        self.destroy()
        self.master.deiconify()

    def command_cancel(self):
        self.destroy()
        self.master.deiconify()
