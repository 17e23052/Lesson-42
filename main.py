word = "sandwich"
guess = ""
not_done = word != guess
guesses = 0

while not_done and guesses < 5:
  guess = input("Guess the word: ")
  if guess == word:
    guesses += 1
    correct = "CORRECT!"
    not_done = False
  else:
    guesses += 1
    correct = "INCORRECT!"

print("You were", correct, "Guesses:", guesses)