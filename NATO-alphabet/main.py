# 1. Create a dictionary in this format:
import pandas
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics = {row.letter:row.code for index, row in data.itterrows()} # create dict

# 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper() # make sure the input is uppercase
output = [phonetics[letter] for letter in user_input]

print(output)