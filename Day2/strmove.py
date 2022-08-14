def strmove(string, count):
    return string[-count:] + string[:-count]
    
print(strmove("hello", 2))    
    