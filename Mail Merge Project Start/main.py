PLACEHOLDER = "[name]"

with open(r"100days-python-coding\Mail Merge Project Start\Input\Names\invited_names.txt") as data:
    name_list = data.readlines()# contains the list of names seperated by newlines and commas

with open(r"100days-python-coding\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    content = file.read()# contains the letter that we would be editing for other users

    for name in name_list:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        with open(f"100days-python-coding/Mail Merge Project Start/output/ReadyToSend/letterto{stripped_name}.txt", mode= "w") as output_files:
            output_letters = output_files.write(new_letter)
