def isPolindrome(s):
    new_str = ""
    for i in range(len(s)):
        if s[i].isalpha() or s[i].isdigit():
            new_str += s[i].lower()

    return new_str == new_str[::-1]
s = 'race a car'

print(isPolindrome(s))               