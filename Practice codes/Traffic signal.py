import time  # Import time module for delay

# Function to simulate the traffic light with a timer
def traffic_light(color):
    color = color.strip().lower()  # Normalize input
    
    if color == "red":
        print("🛑 Stop! The red light is on for 5 seconds...")
        time.sleep(5)  # Pause for 5 seconds
    elif color == "yellow":
        print("⚠️ Get Ready! The yellow light is on for 2 seconds...")
        time.sleep(2)  # Pause for 2 seconds
    elif color == "green":
        print("✅ Go! The green light is on for 5 seconds...")
        time.sleep(5)  # Pause for 5 seconds
    else:
        print("❌ Invalid color! Please enter red, yellow, or green.")

# Simulating a full cycle
colors = ["red", "yellow", "green"]

for signal in colors:
    traffic_light(signal)
    print()  # Newline for readability
