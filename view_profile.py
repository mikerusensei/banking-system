import tkinter as tk
from widgetgenerator import LabelGeneratorGrid, ButtonGeneratorGrid

class View_Profile_Window(tk.Toplevel):
    def __init__(self, master=None, customer_key=None, customer_value=None):
        super().__init__(master)
        self.customer_key = customer_key
        self.customer_value = customer_value
        self.__add_labels()
        self.__add_buttons()
        self.__configure_window()
        

    def __configure_window(self):
        self.title("View Profile")
        self.resizable(False, False)
        self.configure(bg="#C4FFF9")

        for widget in self.winfo_children():
            widget.config(font=("Calibri", 16))

    def __add_labels(self):
        label_configuration = [
            {"text": "[YOUR DETAILS]\n", "column": 0, "row": 0, "bg": "#C4FFF9"},
            {"text": "ID", "column": 0, "row": 1, "bg": "#C4FFF9"},
            {"text": "Fullname", "column": 0, "row": 2, "bg": "#C4FFF9"},
            {"text": "Complete Address", "column": 0, "row": 3, "bg": "#C4FFF9"},
            {"text": "Birthdate", "column": 0, "row": 4, "bg": "#C4FFF9"},
            {"text": "Sex", "column": 0, "row": 5, "bg": "#C4FFF9"},
            {"text": "Nationality", "column": 0, "row": 6, "bg": "#C4FFF9"},
            {"text": "Cellphone Number", "column": 0, "row": 7, "bg": "#C4FFF9"},
            {"text": "Email Address", "column": 0, "row": 8, "bg": "#C4FFF9"},
            {"text": "Username", "column": 0, "row": 9, "bg": "#C4FFF9"},
            {"text": "Password", "column": 0, "row": 10, "bg": "#C4FFF9"},
            {"text": "Verified", "column": 0, "row": 11, "bg": "#C4FFF9"},

            {"text": f"{self.customer_value['id']}", "column": 1, "row": 1, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['name']}", "column": 1, "row": 2, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['address']}", "column": 1, "row": 3, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['birthdate']}", "column": 1, "row": 4, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['gender']}", "column": 1, "row": 5, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['nationality']}", "column": 1, "row": 6, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['cpnumber']}", "column": 1, "row": 7, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['emailaddress']}", "column": 1, "row": 8, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['username']}", "column": 1, "row": 9, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['password']}", "column": 1, "row": 10, "bg": "#C4FFF9"},
            {"text": f"{self.customer_value['verified']}", "column": 1, "row": 11, "bg": "#C4FFF9"},
        ]

        for config in label_configuration:
            LabelGeneratorGrid(self)\
                .set_text(config["text"])\
                .set_pos(config["row"], config["column"])\
                .set_bg_color(config["bg"])\
                .build()

    def __add_buttons(self):
        button_configuration = [
            {"text": "Return", "command": self.command_return, "column": 0, "row": 12, "width": 10, "bg": "#07BEB8"},
        ]

        for config in button_configuration:
            ButtonGeneratorGrid(self)\
                .set_text(config["text"])\
                .set_command(config["command"])\
                .set_pos(config["row"], config["column"])\
                .set_width(config["width"])\
                .set_bg_color(config["bg"])\
                .build()
            
    def command_return(self):
        self.master.deiconify()
        self.destroy()

    def destroy(self):
        super().destroy()
        if self.master:
            self.master.view_profile_window = None
