def str_rev(str):
    arr = list(str)
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]

    # arr 요소들을 이어붙인 문자열을 돌려준다.
    str = "".join(arr)
    return str

# ------------------------
str = 'algorithm'
str1 = str_rev(str)
print(str1)

s = "hello"
s = s[::-1]
print(s)
