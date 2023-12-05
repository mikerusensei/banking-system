from command import Load_CustomerData, Load_SAData, Load_CAData

class Bank:
    __savingsAccounts = Load_SAData()
    __checkingAccounts = Load_CAData()
    __jointAccounts = []
    __customers = Load_CustomerData()

    @staticmethod
    def get_list_savingsAccounts():
        return Bank.__savingsAccounts.execute()
    
    @staticmethod
    def get_list_checkingAccounts():
        return Bank.__checkingAccounts.execute()
    
    @staticmethod
    def get_list_jointAccounts():
        return Bank.__jointAccounts
    
    @staticmethod
    def get_list_customers():
        return Bank.__customers.execute()