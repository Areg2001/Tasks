lst = [1, 3, 4, 1, 5, 3, 7, 8]
def solution(n):
    return sum([n[i] for i in range(len(n)) if n.count(n[i]) == 1])
    
print(solution(lst))
