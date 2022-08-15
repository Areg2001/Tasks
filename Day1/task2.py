with open("text.txt", "r") as f:
    new_code = [row.title() for row in f.readlines()]
    
with open('new.txt', 'w') as f:
    for row in new_code:
        f.write(row)
    
    
    