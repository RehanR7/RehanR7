with open("Input/Names/invited_names.txt", "r") as invited_names:
    name_list = invited_names.readlines()
    for name in name_list:
        name = name.strip()
        with open("Input/Letters/starting_letter.txt", "r") as f:
            letter_content = f.readlines()
            letter_content[0] = letter_content[0].replace("[name]", name)
            letter_content[-1] = letter_content[-1].replace("Angela", "Rehan")
        with open(f"Output/letter_for_{name}", "w") as output_file:
           output_file.writelines(letter_content)
        print(f"Letter for {name} created successfully.")