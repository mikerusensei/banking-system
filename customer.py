from abc import ABC, abstractmethod

class InterfaceCustomer(ABC):
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_address(self):
        pass

    @abstractmethod
    def get_birth_date(self):
        pass

    @abstractmethod
    def get_gender(self):
        pass

    @abstractmethod
    def get_nationality(self):
        pass

    @abstractmethod
    def get_cp_number(self):
        pass

    @abstractmethod
    def get_email_address(self):
        pass


    @abstractmethod
    def add_account(self, account):
        pass

class AbstractCustomer(InterfaceCustomer):
    def __init__(
            self,
            id:str,
            full_name:str,
            full_address:str,
            birth_date:str,
            gender:str,
            nationality:str,
            cp_number:str,
            email_address:str,
            userName:str,
            userPass:str
            ) -> None:
        self.__id = id
        self.__full_name = full_name
        self.__full_address = full_address
        self.__birth_date = birth_date
        self.__gender = gender
        self.__nationality = nationality
        self.__cp_number = cp_number
        self.__email_address = email_address
        self.__userName = userName
        self.__userPass = userPass

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__full_name
    
    def get_address(self):
        return self.__full_address
    
    def get_birth_date(self):
        return self.__birth_date
    
    def get_gender(self):
        return self.__gender
    
    def get_nationality(self):
        return self.__nationality
    
    def get_cp_number(self):
        return self.__cp_number
    
    def get_email_address(self):
        return self.__email_address
    
    def get_username(self):
        return self.__userName
    
    def get_password(self):
        return self.__userPass
    
class Customer(AbstractCustomer):
    def __init__(
            self,  
            id:str,
            full_name: str, 
            full_address: str, 
            birth_date: str, 
            gender: str, 
            nationality: str, 
            cp_number: str, 
            email_address: str, 
            userName: str,
            userPass: str
            ) -> None:
        super().__init__(
            id,
            full_name, 
            full_address, 
            birth_date, 
            gender, 
            nationality, 
            cp_number, 
            email_address, 
            userName,
            userPass
            )
        self.__list_of_acounts = []
        self.__closed_accounts = []
        self.__isUserVerified = False
    

    def add_account(self, account):
        self.__list_of_acounts.append(account)

    def get_list_of_accounts(self):
        return self.__list_of_acounts
    
    def get_closed_accounts(self):
        return self.__closed_accounts
    
    def get_isUserVerified(self):
        return self.__isUserVerified
    
    def set_isUserVerified(self):
        self.__isUserVerified = True

    def set_Unverified(self):
        self.__isUserVerified = False

    def convert_to_dictionary(self):
        return {str(self.get_username()): {
            "id": self.get_id(),
            "name": self.get_name(),
            "address": self.get_address(),
            "birthdate": self.get_birth_date(),
            "gender": self.get_gender(),
            "nationality": self.get_nationality(),
            "cpnumber": self.get_cp_number(),
            "emailaddress": self.get_email_address(),
            "username": self.get_username(),
            "password": self.get_password(),
            "listofaccounts": self.get_list_of_accounts(),
            "verified": self.get_isUserVerified(),
        }}
