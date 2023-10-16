I = input()

N = int(I.split()[0])
T = I.split()[1]

S = [input() for _ in range(N)]

def binary_search(s, t):
    left = 0
    right = len(s) - 1
    #print("~~~~~~~~~~~~~~")
    while left <= right:
        mid = (left + right) // 2
        #print(s[:mid] + s[mid+1:] , t)
        if s[:mid] + s[mid+1:] == t:
            return mid
        elif s[:mid] == t[:mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_a(s, t):
    left = 0
    right = len(s) - 1
    while left <= right:
        mid = (left + right) // 2
        if s[:mid] + s[mid+1:] == t[:mid] + t[mid+1:]:
            return mid
        elif s[:mid] == t[:mid] :
            left = mid + 1
        else:
            right = mid - 1
    return -1


result = []
cnt = 0
for t in S :
    cnt += 1
    if t == T :
        result.append(str(cnt))
    elif len(T)+1 == len(t) :
        if binary_search(t, T) != -1 :
            result.append(str(cnt))
    elif len(T)-1 == len(t) :
        if binary_search(T, t) != -1 :
            result.append(str(cnt))
    elif len(T) == len(t) :
        if binary_search_a(t, T) != -1 :
            result.append(str(cnt))


print(len(result))
print(" ".join(result))