import tkinter as tk
from widgetgenerator import LabelGeneratorPack, ButtonGeneratorPack

class Check_Balance_Window(tk.Toplevel):
    def __init__(self, master=None, customer_key=None, customer_value=None):
        super().__init__(master)
        self.customer_key = customer_key
        self.customer_value = customer_value
        self.__add_labels()
        self.__add_buttons()
        self.__configure_window()
        

    def __configure_window(self):
        self.title("Check Balance")
        self.resizable(False, False)
        self.configure(bg="#C4FFF9")

        for widget in self.winfo_children():
            widget.config(font=("Calibri", 16))

    def __add_labels(self):
        lbl_accountbalances = tk.Label(self, text="[ACCOUNTS AND BALANCES]\n", bg="#C4FFF9")
        lbl_accountbalances.pack(anchor="w")

        for account in self.customer_value['listofaccounts']:
            for key, value in account.items():
                account_key = key
                account_details = value

                LabelGeneratorPack(self)\
                    .set_text(f"Account Id: {account_details['accountid']}\nAccount Balance: {account_details['accountbalance']}\nAccount Type: {account_details['accounttype']}\n Account Status: {account_details['accountstatus']}\n")\
                    .set_anchor("w")\
                    .set_bg_color("#C4FFF9")\
                    .build()
        
    def __add_buttons(self):
        button_configuration = [
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
            
    def command_return(self):
        self.master.deiconify()
        self.destroy()

    def destroy(self):
        super().destroy()
        if self.master:
            self.master.check_balance_window = None
