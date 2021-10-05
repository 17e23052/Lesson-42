from random import choice
from time import sleep

simon_says = []
adding_instructions = True

while adding_instructions:
    instruction = input("Enter a Simon says instruction: ")
    simon_says.append(instruction)
    answer = input("Would you like to add another? Y/N ").upper()
    if answer == "N":
        adding_instructions = False

intros =  ["Simon says...", ""]

for x in range(len(simon_says)):
    print(choice(intros), simon_says[x])
    sleep(3)