# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# import pandas
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
#
# is_on = True
# while is_on:
#     try:
#         word = input("Enter a word: ").upper()
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(output_list)
#         is_on = False
#     except KeyError:
#         print("Sorry, letters in alphabet please.")

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
        word = input("Enter a word: ").upper()
        try:
            output_list = [phonetic_dict[letter] for letter in word]
        except KeyError:
            print("Sorry, letters in alphabet please.")
            generate_phonetic()
        else:
            print(output_list)

generate_phonetic()
