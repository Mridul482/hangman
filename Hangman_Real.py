import random
from HangmanWords import words
from HangmanVisuals import lives_visual
import string
#words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","deserted","detailed","determined","devilish","didactic","different","difficult","diligent","dirty","disagreeable","disastrous"]


def get_valid_word(words):
		word = random.choice(words)  # randomly chooses something from the list
		while "-" in word or " " in word:
				word = random.choice(words)
		return word.upper()

def hangman():
		word = get_valid_word(words)
		word_letters = set(word)  # letters in the word
		alphabet = set(string.ascii_uppercase)
		used_letters = set()  # what the user has guessed
		lives = 5
		score = 0

		# getting user input

		while len(word_letters) > 0 and lives > 0: 
				print("Welcome to Mridul's Hangman")
				print(f"You have these many lives left: {lives}") #printing and sorting the used letters
				print("You have used these letters: ", ' '.join(sorted(used_letters))) 
				# what current word is (ie W - R D)
				word_list = [letter if letter in used_letters else '-' for letter in word]
				print(lives_visual[lives])
				print("Current word: ", " ".join(word_list))

				user_letter = input("Guess a letter: ").upper()
				if user_letter in alphabet - used_letters:
						used_letters.add(user_letter)
						if user_letter in word_letters:
								word_letters.remove(user_letter)
								print('')
						else: #takes away a life if the person gets it wrong
							lives = lives - 1 
							print("\nYou have already used that letter!")

				elif user_letter in used_letters:
					print("\nYou have already used that letter. Guess another letter.")

				else:
					print("\nThat is not a valid letter.")
		if lives == 0:
			print(lives_visual[lives])
			print("\ngame over :(")
			print("\nSorry you have reached the maximum number of incorrect guesses")
			print("\nThe word was "+ word)
		else:
			print(f"Congratualtions! You have guessed the correct word! of {word} !")
			score += 1
			print(f"Your score is {score}")
		
		playagain = input("Do you want to play again? ").lower()
		if playagain == "yes":
			hangman()

if __name__ == '__main__':
		hangman()