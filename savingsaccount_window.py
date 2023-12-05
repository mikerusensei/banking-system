import tkinter as tk
import datetime
from tkinter import messagebox
from account import SavingsAccount
from bank import Bank
from widgetgenerator import LabelGeneratorPack
from functions import save_savingsaccount_data, save_customer_data

class SavingsAccount_Window(tk.Toplevel):
    def __init__(self, master=None, customer_key=None, customer_value=None):
        super().__init__(master)
        self.customer_key = customer_key
        self.customer_value = customer_value
        self.today = datetime.date.today()
        self.current_year = self.today.year
        self.__savings_list = Bank.get_list_savingsAccounts()
        self.account = SavingsAccount(f"{self.current_year}-1{len(self.__savings_list)+1}")
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
            {"text": f"Savings Account\n", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"Terms and Condition\n", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"- Initial deposit of PHP 500.", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"- Maintaining balance of PHP 2000.", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"- Withdrawal limit of PHP 20000 per day.", "anchor": "w", "bg": "#C4FFF9"},
            {"text": f"- Account will be closed if the balance falls to PHP 0.\n", "anchor": "w", "bg": "#C4FFF9"},
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

        if initial_deposit >= 500: 
            account_balance += initial_deposit
            self.account.set_accountBalance(account_balance)
            self.account.set_open()
            self.account.get_accountHolders().append(self.customer_value["id"])
            account_dictionary = self.account.convert_to_dictionary()

            self.customer_value["listofaccounts"].append(account_dictionary)
            self.customer_value["verified"] = True
            self.__savings_list.update(account_dictionary)
            save_savingsaccount_data(self.__savings_list)
            save_customer_data({self.customer_key: self.customer_value})
            self.master.deiconify()
            self.destroy()
        else:
            messagebox.showerror("Error", "Initial deposit must be Php 500!")

