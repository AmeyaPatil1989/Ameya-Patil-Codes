import time
from datetime import datetime

# Get user input for alarm time
alarm_hour = int(input("Enter the hour for the alarm (0-23): "))
alarm_minute = int(input("Enter the minute for the alarm (0-59): "))

print(f"⏳ Alarm set for {alarm_hour:02d}:{alarm_minute:02d}. Waiting...")

# Infinite loop to continuously check the time
while True:
    now = datetime.now()  # Get current time
    current_hour = now.hour
    current_minute = now.minute

    # Check if current time matches the alarm time
    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("\n⏰ WAKE UP! ALARM RINGING! ⏰")
        break  # Exit the loop after alarm triggers

    time.sleep(30)  # Check time every 30 seconds (to avoid CPU overuse)
