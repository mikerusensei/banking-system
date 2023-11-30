class Bank:
    __savingsAccounts = []
    __checkingAccounts = []
    __jointAccounts = []
    __customers =[]

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