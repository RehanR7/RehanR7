import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
df_dict = {row.letter:row.code for (index, row) in df.iterrows()}
word = input("Enter the Word: ").upper()
output = [df_dict[letter] for letter in word]
print(output)