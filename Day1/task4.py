count = 0
with open("text.txt", "r") as f:
    file_code = [row.strip() for row in f.readlines()]
    for i in range(len(file_code)):
        line_member = list(file_code[i])
        for j in range((len(line_member))):
            if line_member[j].isalpha():
                count += 1
    print(count)
    