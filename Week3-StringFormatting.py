#!/usr/bin/env python3

# Here are the variables:

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

"""
The following is an output to each question that is in the Week 3 Lab. I will have the question in the script but
will block its output. The following line will be the "answer" or the line of Python code that will output exactly what the 
question says.

"""
# Question 1: 'Hello Timmy;
print(f"Hello {varName}")

# Question 2: 'Red-Green-Blue'
print(f"{varRed}-{varGreen}-{varBlue}")

# Question 3: 'Is this green or blue?'
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")

# Question 4: 'My name is TIMMY'
print(f"My name is {varName.upper()}")

# Question 5: '[++Red++]'
print(f"[{varRed:+^7s}]")

# Question 6: '[green==]'
print(f"[{varGreen.lower()}==]")

# Question 7: '[*****blue]'
print(f"[{varBlue.lower():*>9s}]")

# Question 8: 'BlueBlueBlueBlueBlueBlueBlueBlueBlueBlue'
print(f"{varBlue*10}")

# Question 9: '10.4516295'
print(varLoot)

# Question 10: '10.5'
print(f"{varLoot:>.1f}")

# Question 11: 'I have $10.45'
print(f"I have ${varLoot:>.4}")

# Question 12: '[$$$Red$$$$][$$Green$$$][$$$Blue$$$]'
print(f"[{varRed:$^10s}][{varGreen:$^10s}][{varBlue:$^10s}]")

# Question 13: '[  deR  ][  Green  ][  eulB  ]'
print(f"[  {varRed[::-1]}  ][  {varGreen}  ][  {varBlue[::-1]}  ]")

# Question 14: 'First Color:[Red] Second Color:[Green] Third Color:[Blue]'
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")

