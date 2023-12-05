from tkinter import messagebox
from abc import ABC, abstractmethod
import os
import json

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class MessageBoxAskQuestion(Command):
    def __init__(self, message) -> None:
        self.__message = message
    
    def execute(self):
        return messagebox.askquestion(title="Trial", message=self.__message)

class MessageBoxShowError(Command):
    def __init__(self, message) -> None:
        self.__message = message

    def execute(self):
        return messagebox.showerror(title="Error", message=self.__message)


class Save_CustomerData(Command):
    def __init__(self, person_data) -> None:
        self.person_data = person_data

    def execute(self):
        if os.path.exists("person_data.json"):
            with open("person_data.json", "r") as file:
                existing_data = json.load(file)
                existing_data.update(self.person_data)
            
            with open("person_data.json", "w") as file:
                json.dump(existing_data, file, indent=4)
        else:
            with open("person_data.json", "w") as file:
                json.dump(self.person_data, file, indent=4)
    
class Load_CustomerData(Command):
    def execute(self):
        if os.path.exists("person_data.json"):
            with open("person_data.json", "r") as file:
                return json.load(file)
        else:
            return {}
    
class Save_SAData(Command):
    def __init__(self, account_data):
        self.account_data = account_data

    def execute(self):
        if os.path.exists("savingsaccount_data.json"):
            with open("savingsaccount_data.json", "r") as file:
                existing_data = json.load(file)
                existing_data.update(self.account_data)

            with open("savingsaccount_data.json", "w") as file:
                json.dump(self.account_data, file, indent=4)
        else:
            with open("savingsaccount_data.json", "w") as file:
                json.dump(self.account_data, file, indent=4)
    
class Load_SAData(Command):
    def execute(self):
        if os.path.exists("savingsaccount_data.json"):
            with open("savingsaccount_data.json", "r") as file:
                return json.load(file)
        else:
            return {}
        
class Save_CAData(Command):
    def __init__(self, account_data):
        self.account_data = account_data

    def execute(self):
        if os.path.exists("checkingaccount_data.json"):
            with open("checkingaccount_data.json", "r") as file:
                existing_data = json.load(file)
                existing_data.update(self.account_data)

            with open("checkingaccount_data.json", "w") as file:
                json.dump(self.account_data, file, indent=4)
        else:
            with open("checkingaccount_data.json", "w") as file:
                json.dump(self.account_data, file, indent=4)

class Load_CAData(Command):
    def execute(self):
        if os.path.exists("checkingaccount_data.json"):
            with open("checkingaccount_data.json", "r") as file:
                return json.load(file)
        else:
            return {}