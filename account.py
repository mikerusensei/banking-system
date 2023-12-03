from abc import ABC, abstractmethod

class InterfaceAccount(ABC):
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_accountType(self):
        pass

    @abstractmethod
    def get_accountHolders(self):
        pass

    @abstractmethod
    def get_accountBalance(self):
        pass
        
    @abstractmethod
    def get_status(self):
        pass

class AbstractAccount(InterfaceAccount):
    def __init__(self, id, accountType) -> None:
        self.__id = id
        self.__accountType = accountType
        self.__account_holders = []
        self.__account_balance = 0
        self.__status = 'closed'

    def get_id(self):
        return self.__id
    
    def get_accountType(self):
        return self.__accountType
    
    def get_accountHolders(self):
        return self.__account_holders
    
    def get_accountBalance(self):
        return self.__account_balance
    
    def set_accountBalance(self, balance):
        self.__account_balance = balance
    
    def get_status(self):
        return self.__status
    
    def set_open(self):
        self.__status = 'opened'

    def set_close(self):
        self.__status = 'closed'

    def convert_to_dictionary(self):
        return {str(self.get_id()): {
            "accountid": self.get_id(),
            "accounttype": self.get_accountType(),
            "accountbalance": self.get_accountBalance(),
            "accountholder/s": self.get_accountHolders(),
            "accountstatus": self.get_status(),
        }}
        
class SavingsAccount(AbstractAccount):
    def __init__(self, id) -> None:
        super().__init__(id, "Savings Account")

class CheckingAccount(AbstractAccount):
    def __init__(self, id) -> None:
        super().__init__(id, "Checking Account")

class JointAccount(AbstractAccount):
    def __init__(self, id) -> None:
        super().__init__(id, "Joint Account")

    def add_customer(self, customer):
        self.get_accountHolders().append(customer)