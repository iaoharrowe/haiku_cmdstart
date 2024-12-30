import os
import random

# Dynamically get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the haiku database
haiku_file_path = os.path.join(script_dir, "haiku_~.txt")

# Load haiku database
try:
    with open(haiku_file_path, "r", encoding="utf-8") as file:
        haikus = file.read().strip().split("\n---\n")
except FileNotFoundError:
    print(f"Error: haiku_~.txt not found at {haiku_file_path}")
    exit()

# Select and print a random haiku
random_haiku = random.choice(haikus)
print(random_haiku.strip())

