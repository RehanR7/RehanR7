with open("./Input/Names/invited_names.txt") as invited_names:
    name_list = invited_names.readlines()
    for name in name_list:
        striped_name = name.strip()
        with open("./Input/Letters/starting_letter.txt") as starting_letter:
            letter_contents = starting_letter.read()
            replace_name = letter_contents.replace("[name]", striped_name)
        with open(f"./Output/ReadyToSend/Letter_for_{striped_name}.txt", "w") as completed_letter:
            completed_letter.write(replace_name)