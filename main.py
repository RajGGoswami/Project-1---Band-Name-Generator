# Day 1 – Band Name Generator
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Understand how to print output to the console
# - Take user input using input()
# - Store user input in variables
# - Combine (concatenate) strings to create a final output
#
# This is intentionally simple to reflect my early learning stage.
# Later projects improve structure, validation, and reusability.

print("Welcome to the Band Name Generator.")

# Ask the user for the city they grew up in and store the input
city_name = input("What's the name of the city you grew up in?\n")

# Ask the user for their pet's name and store the input
pet_name = input("What's your pet name?\n")

# Combine the city name and pet name to generate a band name
print("Your band name could be " + city_name + " " + pet_name)
