# Import the datetime and time modules
import datetime
import time

# Prompt the user to enter the first date-time
date1 = input("Enter the first date-time (in the format YYYY-MM-DD HH:MM): ")

# Convert the first date-time to a datetime object
datetime1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M")

# Create a datetime object for the current time
current_time = datetime.datetime.now()

# Prompt the user to select the current time or enter a custom time
choice = input(
    "Select the current time (enter 'c') or enter a custom time (enter 'custom'): ")

if choice == "c":
    # Use the current time as the second date-time
    datetime2 = current_time
else:
    # Prompt the user to enter a custom time
    date2 = input(
        "Enter the second date-time (in the format YYYY-MM-DD HH:MM): ")

    # Convert the second date-time to a datetime object
    datetime2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M")

# Calculate the difference between the two date-times in minutes
diff = datetime2 - datetime1
minutes = diff.total_seconds() / 60.0

# Print the result
print(f"There are {minutes} minutes between the two date-times.")
