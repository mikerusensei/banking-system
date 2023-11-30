from time import strftime
from datetime import datetime

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