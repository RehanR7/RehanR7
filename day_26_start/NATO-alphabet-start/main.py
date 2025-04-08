import pandas

#TODO 1. Create a dictionary in this format:
file = pandas.read_csv("nato_phonetic_alphabet.csv")
# letter = []
# code = []
# for (index, row) in file.iterrows():
#     letter.append(row.letter)
#     code.append(row.code)
#
# dic_file = {key:value for (key, value) in zip(letter,code)}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_input = input("Write the word here: ").strip()
# phonetic_list = [dic_file[letter.upper()] for letter in user_input if letter.upper() in dic_file]
# print(phonetic_list)

phonetic_dict = {row.letter:row.code for (index, row) in file.iterrows()}
word = input("Enter the Word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)