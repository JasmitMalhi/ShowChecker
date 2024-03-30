from random import choice

# Create list of shows
shows = [['AA', 'BB', 'CC'],
         ['DD', 'EE', 'FF'],
         ['GG', 'HH', 'II']]

print("What mood are you in?")
mood = input()

found = False  # Initialize a flag to track if any match is found

for item in shows:
    if mood in item:
        print(mood + ' show: ' + item[0])
        found = True  # Set the flag to True if a match is found

if not found:
    print("Sorry, no shows match your mood.")
