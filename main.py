word = "sandwich"
guess = ""
not_done = word != guess #not done when the guess does not equal the word
guesses = 0

while not_done and guesses < 5: #if the word is not guessed and less than 5 guesses
  guess = input("Guess the word: ")
  if guess == word:
    guesses += 1
    correct = "CORRECT!"
    not_done = False #if guessed correctly, the loop finishes
  else:
    guesses += 1
    correct = "INCORRECT!"

print("You were", correct, "Guesses:", guesses)