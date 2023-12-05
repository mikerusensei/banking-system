from time import strftime
from datetime import datetime
import os
import json

def current_time(time_label):
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    time_label.after(1000, lambda: current_time(time_label))

def greet():
    current_time = datetime.strptime(strftime("%I:%M:%S %p"), "%I:%M:%S %p").time()

    afternoon_time = datetime.strptime("12:00:00 PM", "%I:%M:%S %p").time()
    evening_time = datetime.strptime("6:00:00 PM", "%I:%M:%S %p").time()

    if current_time < afternoon_time:
        return "Good Morning!"
    elif current_time < evening_time:
       return "Good Afternoon!"
    else:
        return "Good Evening!"
    
def save_customer_data(person_data):
    if os.path.exists("person_data.json"):
        with open("person_data.json", "r") as file:
            existing_data = json.load(file)
            existing_data.update(person_data)
        
        with open("person_data.json", "w") as file:
            json.dump(existing_data, file, indent=4)
    else:
        with open("person_data.json", "w") as file:
            json.dump(person_data, file, indent=4)


def load_customer_data():
    if os.path.exists("person_data.json"):
        with open("person_data.json", "r") as file:
            return json.load(file)
    else:
        return {}
    
def save_savingsaccount_data(account_data):
    if os.path.exists("savingsaccount_data.json"):
        with open("savingsaccount_data.json", "r") as file:
            existing_data = json.load(file)
            existing_data.update(account_data)

        with open("savingsaccount_data.json", "w") as file:
            json.dump(account_data, file, indent=4)
    else:
        with open("savingsaccount_data.json", "w") as file:
            json.dump(account_data, file, indent=4)

def load_savingsaccount_data():
    if os.path.exists("savingsaccount_data.json"):
        with open("savingsaccount_data.json", "r") as file:
            return json.load(file)
    else:
        return {}
    