from boot import boot
from messages import get_status
import moods


print("====================================")
print("           VIRAMIND v0.1            ")
print("====================================")

boot()

print("Status Today: ")
print(get_status())

current_mood = moods.get_random_mood()

print()
print("Loading Personality Engine...")
print(f"Personality Selected: {moods.get_emoji(current_mood)} {current_mood}")
print(moods.get_message(current_mood, "startup"))

print()
print("System Ready.")

print("Drink some coffee.")
print("Type 'Help' to begin")
print()
while True:
    user_input = input("Viramind > ")
    
    # Check for the exit condition
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
        
    print("Complier error: though it would be funny.")