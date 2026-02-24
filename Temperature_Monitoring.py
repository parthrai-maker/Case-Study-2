import random
import time


min_limit = float(input("Enter minimum temperature limit: "))
max_limit = float(input("Enter maximum temperature limit: "))

print("\nStarting IoT Temperature Monitoring System...\n")

while True:
   
    temperature = round(random.uniform(-10, 60), 2)
    
    print(f"Current Temperature: {temperature} °C")
    
   
    if temperature < min_limit:
        print("⚠ ALERT: Temperature is BELOW minimum limit!\n")
    elif temperature > max_limit:
        print("⚠ ALERT: Temperature is ABOVE maximum limit!\n")
    else:
        print("✅ Temperature is within safe range.\n")
   
    time.sleep(2)