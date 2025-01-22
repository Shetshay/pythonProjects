    # student_dict = {
    #     "student": ["Angela", "James", "Lily"],
    #     "score": [56, 76, 98]
    # }
    #
    # #Looping through dictionaries:
    # for (key, value) in student_dict.items():
    #     #Access key and value
    #     pass
    #
    # import pandas
    # student_data_frame = pandas.DataFrame(student_dict)
    #
    # #Loop through rows of a data frame
    # for (index, row) in student_data_frame.iterrows():
    #     #Access index and row
    #     #Access row.student or row.score
    #     pass

    # Keyword Method with iterrows()
    # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
import pandas
{"A": "Alfa", "B": "Bravo"}
phonetics = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics_dict = {} # create dict
for (index, row) in phonetics.iterrows():
    #Access index and row
    phonetics_dict.update({row.letter:row.code}) # create a new dictionary and put the row.letter/row.code as key/value
    #Access row.letter or row.code
print(phonetics_dict) # print the final result of that

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper() # make sure the input is uppercase
output = [] # instantiate output array for later use
arrayed_user_input = list(user_input) # make the user input a list/array

phonetics_array = [key for key in phonetics_dict.keys()] # dict comprehension to create an array of keys
    # from phonetics dict

for array_number_pos in range(len(arrayed_user_input)): # loop through the length of the input
    if arrayed_user_input[array_number_pos] in phonetics_array: # if the array of the user_input at [0,1,2...] is in the
        # phonetics array, add it to the output array that we instantiated earlier
        output.append(phonetics_dict.get(arrayed_user_input[array_number_pos])) # grab the correct phonetic
        # using the letter
print(output)