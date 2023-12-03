from functions import load_customer_data, load_savingsaccount_data

class Bank:
    __savingsAccounts = load_savingsaccount_data()
    __checkingAccounts = []
    __jointAccounts = []
    __customers = load_customer_data()

    @staticmethod
    def get_list_savingsAccounts():
        return Bank.__savingsAccounts
    
    @staticmethod
    def get_list_checkingAccounts():
        return Bank.__checkingAccounts
    
    @staticmethod
    def get_list_jointAccounts():
        return Bank.__jointAccounts
    
    @staticmethod
    def get_list_customers():
        return Bank.__customers