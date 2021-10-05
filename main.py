from random import choice
from time import sleep

simon_says = [] #starts the list of instructions
adding_instructions = True

while adding_instructions:
    instruction = input("Enter a Simon says instruction: ")
    simon_says.append(instruction) #appends the instruction to the 'simon_says' list
    answer = input("Would you like to add another? Y/N ").upper()
    if answer == "N":
        adding_instructions = False #the while loop ends if no more inst. are requested

intros =  ["Simon says...", ""]

for x in range(len(simon_says)):
    print(choice(intros), simon_says[x])
    sleep(3)
#prints either 'Simon says...' or nothing, then the instruction. It waits before executing the next one, and repeating until all instructions are shown.