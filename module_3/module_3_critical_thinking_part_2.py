import numpy as np  

# Part 2: Alarm Clock Program  
print("Alarm Clock")  

# Get the current time and wait time  
current_time = int(input("What is the current time (in 24-hour format)? "))  
wait_time = int(input("Enter wait time (in hours): "))

# Calculate alarm time  
alarm_time = (current_time + wait_time) % 24  

# Dynamically calculate a message based on what time of day the alarm clock will go off
if 5 <= alarm_time < 12:
    message = "Good morning!"
elif 12 <= alarm_time < 18:
    message = "Good afternoon!"
else:
    message = "Good night!"

# Print alarm time and message
print(f"Your alarm will go off at {alarm_time}:00 on a 24-hour clock. {message}")
  

