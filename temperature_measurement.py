import random
import time

def monitor_temperature(lower, upper):
    print("\nMonitoring temperature...")
    print(f"Lower limit: {lower}°C, Upper limit: {upper}°C\n")

    while True:
        temperature = random.uniform(lower - 5, upper + 5)  # Simulate temp variation
        temperature = round(temperature, 2)
        
        print(f"Current Temperature: {temperature}°C")
        
        if temperature < lower:
            print("⚠ Alert: Temperature is BELOW the lower limit!")
        elif temperature > upper:
            print("🔥 Alert: Temperature is ABOVE the upper limit!")
        else:
            print("✅ Temperature is within the safe range.")
        
        time.sleep(2)  # Delay for readability

# Take temperature limits from the user
lower_limit = float(input("Enter the lower temperature limit (°C): "))
upper_limit = float(input("Enter the upper temperature limit (°C): "))

monitor_temperature(lower_limit, upper_limit)