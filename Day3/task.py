with open("file.txt", "r") as current:
    with open("file2.txt.", 'w') as file2:
        file_text = current.readlines()
        file_text = [word.title() for word in file_text]
        file2.write(str(file_text))




