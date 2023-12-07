import tkinter as tk
from tkinter import messagebox
from bank import Bank
from command import Save_SAData, Save_CAData, Save_CustomerData
from widgetgenerator import FrameGeneratorGrid, LabelGeneratorPack, EntryGeneratorPack, ButtonGeneratorPack

class Withdraw_Window(tk.Toplevel):
    def __init__(self, master=None, customer_key=None, customer_value=None):
        super().__init__(master)
        self.customer_key = customer_key
        self.customer_value = customer_value
        self.__savings_list = Bank.get_list_savingsAccounts()
        self.__checking_list = Bank.get_list_checkingAccounts()
        self.__add_frames()
        self.__add_labels()
        self.__add_buttons()
        self.__configure_window()

    def __configure_window(self):
        self.title("Deposit")
        self.resizable(False, False)
        self.configure(bg="#C4FFF9")
        self.accounts_frame.config(bg="#C4FFF9")
        self.deposit_frame.config(bg="#C4FFF9")

        for widget in self.accounts_frame.winfo_children():
            widget.config(font=("Calibri", 16))

        for widget in self.deposit_frame.winfo_children():
            widget.configure(font=("Calibri", 16))

    def __add_frames(self):
        self.accounts_frame = FrameGeneratorGrid(self)\
            .set_pos(column=0, row=0)\
            .build()
        
        self.deposit_frame = FrameGeneratorGrid(self)\
            .set_pos(column=1, row=0)\
            .build()
        
    def __add_labels(self):
        lbl_accountbalances = tk.Label(self.accounts_frame, text="[ACCOUNTS AND BALANCES]\n", bg="#C4FFF9")
        lbl_accountbalances.pack(anchor="w")

        for account in self.customer_value['listofaccounts']:
            for key, value in account.items():
                account_key = key
                account_details = value
                LabelGeneratorPack(self.accounts_frame)\
                    .set_text(f"Account Id: {account_details['accountid']}")\
                    .set_anchor("w")\
                    .set_bg_color("#C4FFF9")\
                    .build()
                
                LabelGeneratorPack(self.accounts_frame)\
                    .set_text(f"Account Balance: {account_details['accountbalance']}")\
                    .set_anchor("w")\
                    .set_bg_color("#C4FFF9")\
                    .build()
                
                LabelGeneratorPack(self.accounts_frame)\
                    .set_text(f"Account Type: {account_details['accounttype']}")\
                    .set_anchor("w")\
                    .set_bg_color("#C4FFF9")\
                    .build()
                
                LabelGeneratorPack(self.accounts_frame)\
                    .set_text(f"Account Status: {account_details['accountstatus']}\n")\
                    .set_anchor("w")\
                    .set_bg_color("#C4FFF9")\
                    .build()
            
        LabelGeneratorPack(self.deposit_frame)\
            .set_anchor("w")\
            .set_text("[WITHDRAWAL]\n")\
            .set_bg_color("#C4FFF9")\
            .build()
        
        LabelGeneratorPack(self.deposit_frame)\
            .set_anchor("w")\
            .set_text("Enter account id")\
            .set_bg_color("#C4FFF9")\
            .build()
        
        self.account_id_entry = EntryGeneratorPack(self.deposit_frame)\
            .set_anchor("w")\
            .build()
        
        LabelGeneratorPack(self.deposit_frame)\
            .set_anchor("w")\
            .set_text("Enter amount")\
            .set_bg_color("#C4FFF9")\
            .build()
        
        self.amount_entry = EntryGeneratorPack(self.deposit_frame)\
            .set_anchor("w")\
            .build()
        
    def __add_buttons(self):
        button_configuration = [
            {"text": "Return", "command": self.command_return, "anchor": "w", "width": 15, "bg": "#07BEB8"},
            {"text": "Submit", "command": self.command_submit, "anchor": "w", "width": 15, "bg": "#07BEB8"},
        ]

        for config in button_configuration:
            ButtonGeneratorPack(self.deposit_frame)\
                .set_text(config["text"])\
                .set_command(config["command"])\
                .set_anchor(config["anchor"])\
                .set_width(config["width"])\
                .set_bg_color(config["bg"])\
                .build()
            
    def command_submit(self):
        account_id_inputted = self.account_id_entry.get()
        ammount_inputted = self.amount_entry.get()
        found_account = False

        for account in self.customer_value['listofaccounts']:
            for key, value in account.items():
                account_details = value

                if key == account_id_inputted:
                    found_account = True
                    current_balance = int(account_details['accountbalance'])
                    current_balance -= int(ammount_inputted)
                    account_details['accountbalance'] = current_balance

                    if account_details['accounttype'] == 'Savings Account':
                        if current_balance == 0:
                            account_details["accountstatus"] = 'closed'
                            self.customer_value["closedaccounts"].append({key: account_details})
                            self.customer_value["listofaccounts"].remove({key: account_details})
                            self.__savings_list.update({key: account_details})
                            save_account = Save_SAData(self.__savings_list)
                            save_customer = Save_CustomerData({self.customer_key: self.customer_value})
                            save_customer.execute()
                            save_account.execute()
                            self.master.deiconify()
                            self.destroy()
                            break
                        else:
                            self.__savings_list.update({key: account_details})
                            save_account = Save_SAData(self.__savings_list)
                            save_customer = Save_CustomerData({self.customer_key: self.customer_value})
                            save_account.execute()
                            save_customer.execute()
                            self.master.deiconify()
                            self.destroy()
                            break
                    elif account_details['accounttype'] == 'Checking Account':
                        if current_balance == 0:
                            account_details["accountstatus"] = 'closed'
                            self.customer_value["closedaccounts"].append(account_details)
                            self.customer_value["listofaccounts"].remove(account)
                            self.__checking_list.update({key: account_details})
                            save_account = Save_CAData(self.__checking_list)
                            save_customer = Save_CustomerData({self.customer_key: self.customer_value})
                            save_customer.execute()
                            save_account.execute()
                            self.master.deiconify()
                            self.destroy()
                            break
                        else:
                            self.__checking_list.update({key: account_details})
                            save_account = Save_CAData(self.__checking_list)
                            save_customer = Save_CustomerData({self.customer_key: self.customer_value})
                            save_account.execute()
                            save_customer.execute()
                            self.master.deiconify()
                            self.destroy()
                            break

        if not found_account:
            messagebox.showerror("Error", f"Account was not found!")

    def command_return(self):
        self.master.deiconify()
        self.destroy()

    def destroy(self):
        super().destroy()
        if self.master:
            self.master.withdraw_window = None
    