haystack = "hello"
needle = "elloo"
def indexOfstr(str1, str2):
    if str2 in str1 or str1 in str2:
        return str1.index(str2)
    return -1
print(indexOfstr(haystack, needle))        

