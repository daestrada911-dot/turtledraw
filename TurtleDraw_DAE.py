# ==========================================
# TurtleDraw_de.py
# Author: Diego Estrada
# Description:
#   Reads a user-provided text file containing turtle drawing commands,
#   draws lines and color changes accordingly, handles 'stop' commands,
#   and prints the total distance traveled.
# ==========================================

import turtle
import math
import os

# --- REQUIREMENT 1: Basic setup ---
print("🐢 TurtleDraw_de Starting...\n")

# Set up turtle window 450x450
screen = turtle.Screen()
screen.setup(450, 450)
screen.title("TurtleDraw_de - by Diego Estrada")

# Create the turtle
artist = turtle.Turtle()
artist.speed(0)  # 0 = max speed
artist.penup()

# --- REQUIREMENT 2: Ask for filename and read the file ---
filename = input("Enter the name of the input file (e.g. turtle-draw.txt): ").strip()

# Check if file exists
if not os.path.exists(filename):
    print(f"⚠️ File '{filename}' not found. Please check and try again.")
    turtle.bye()
else:
    print(f"\n✅ Reading from '{filename}'...\n")

    total_distance = 0.0
    last_x, last_y = 0, 0
    first_move = True

    with open(filename, "r") as file:
        for line in file:
            # Strip whitespace (Requirement 2)
            line = line.strip()

            # Skip empty lines
            if line == "":
                continue

            # Split line into parts (Requirement 2)
            parts = line.split(" ")

            # --- REQUIREMENT 3: Handle "stop" and color commands ---
            if len(parts) == 1 and parts[0].lower() == "stop":
                artist.penup()
                print("✋ Stop command detected: lifting pen.")
                continue

            elif len(parts) == 3:
                color = parts[0]
                try:
                    x = int(parts[1])
                    y = int(parts[2])
                except ValueError:
                    print(f"⚠️ Invalid coordinates: {line}")
                    continue

                # Move to first point without drawing (Requirement 3)
                if first_move:
                    artist.goto(x, y)
                    artist.pendown()
                    first_move = False
                else:
                    # Calculate distance only when drawing (Requirement 4)
                    distance = math.sqrt((x - last_x) ** 2 + (y - last_y) ** 2)
                    total_distance += distance
                    artist.pencolor(color)
                    artist.goto(x, y)

                last_x, last_y = x, y

            else:
                print(f"⚠️ Invalid command: {line}")

    # --- REQUIREMENT 4: Print total distance on screen ---
    artist.penup()
    artist.goto(120, -200)  # Bottom right area of the window
    artist.color("black")
    artist.write(f"Total Distance: {total_distance:.2f}", font=("Arial", 12, "normal"))

    # Close the file and wait for user
    print(f"\n✅ Drawing complete! Total distance = {total_distance:.2f}")
    print("Press Enter in this console window to close the turtle screen.")
    input("→ Press Enter to exit... ")
    turtle.bye()
