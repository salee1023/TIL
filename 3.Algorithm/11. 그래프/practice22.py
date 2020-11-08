def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return int(a*b/gcd(a, b))

def solution(arr):
    answer = arr[0]
    for i in range(len(arr)):
        answer = lcm(answer, arr[i])
    return answer

print(solution([2,6,8,14]))