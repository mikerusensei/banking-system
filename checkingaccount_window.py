import tkinter as tk
import datetime
from tkinter import messagebox
from account import CheckingAccount
from bank import Bank
from widgetgenerator import LabelGeneratorPack
from command import Save_CAData, Save_CustomerData

class CheckingAccount_Window(tk.Toplevel):
    def __init__(self, master=None, customer_key=None, customer_value=None):
        super().__init__(master)
        self.customer_key = customer_key
        self.customer_value = customer_value
        self.today = datetime.date.today()
        self.current_year = self.today.year
        self.__checking_list = Bank.get_list_checkingAccounts()
        self.account = CheckingAccount(f"{self.current_year}-2{len(self.__checking_list)+1}")
        self.__add_labels()
        self.__add_checkbox()
        self.__add_entries()
        self.__add_buttons()
        self.__configure_window()

    def __configure_window(self):
        self.title("Enroll Account")
        self.resizable(False, False)
        self.configure(bg="#C4FFF9")

        for widget in self.winfo_children():
            widget.config(font=("Calibri", 16))

    def __add_labels(self):
        label_configuration = [
            {"text": f"Checking Account\n", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"Terms and Condition\n", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"- Initial deposit of PHP 25000.", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"- No withdrawal limit per day.", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"- Account will be closed if the balance falls to PHP 0.", "anchor": "w", "bg": "#C4FFF9"},            
        ]

        for config in label_configuration:
            LabelGeneratorPack(self)\
                .set_text(config["text"])\
                .set_anchor(config["anchor"])\
                .set_bg_color(config["bg"])\
                .build()
            
    def __add_checkbox(self):
        self.checkbox_variable = tk.IntVar()
        checkbox = tk.Checkbutton(self, text="Do you accept?", variable=self.checkbox_variable, command=self.check_checbox, bg="#C4FFF9")
        checkbox.pack(anchor="w")

    def __add_entries(self):
        lbl_initial_deposit = tk.Label(self, text="\nEnter initial deposit", bg="#C4FFF9")
        lbl_initial_deposit.pack(anchor="w")

        self.initial_deposit_entry = tk.Entry(self, state=tk.DISABLED)
        self.initial_deposit_entry.pack(anchor="w")

    def __add_buttons(self):
        self.btn_submit = tk.Button(self, text="Submit", command=self.command_submit, state=tk.DISABLED, width=15, bg="#07BEB8")
        self.btn_submit.pack(anchor="w")

    def check_checbox(self):
        if self.checkbox_variable.get() == 1:
            self.initial_deposit_entry.config(state=tk.NORMAL)
            self.btn_submit.config(state=tk.NORMAL)
        else:
            self.initial_deposit_entry.config(state=tk.DISABLED)
            self.btn_submit.config(state=tk.DISABLED)

    def command_submit(self):
        initial_deposit_entry = self.initial_deposit_entry.get()
        initial_deposit = int(initial_deposit_entry)
        account_balance = int(self.account.get_accountBalance())

        if initial_deposit >= 25000:
            account_balance += initial_deposit
            self.account.set_accountBalance(account_balance)
            self.account.set_open()
            self.account.get_accountHolders().append(self.customer_value['id'])
            account_dictionary = self.account.convert_to_dictionary()

            self.customer_value["listofaccounts"].append(account_dictionary)
            self.customer_value["verified"] = True
            self.__checking_list.update(account_dictionary)
            checkingaccount_data = Save_CAData(self.__checking_list)
            customer_data = Save_CustomerData({self.customer_key: self.customer_value})
            checkingaccount_data.execute()
            customer_data.execute()
            self.master.deiconify()
            self.destroy()
        else:
            messagebox.showerror("Error", "Initial deposit must be Php 25000!")
