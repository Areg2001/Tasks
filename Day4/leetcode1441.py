def buildArray(target, n):
    lst = []
    for i in range(1, min(target[-1], n) + 1):
        if i in target:
            lst.append("Push")
        else:
            lst.extend(["Push", "Pop"])
    return lst

print(buildArray([1,3,4], 5))
