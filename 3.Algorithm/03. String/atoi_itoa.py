# 문자 -> 정수
def atoi(str): 
    value = 0
    for i in range(len(str)):
        c = str[i]
        if '0' <= c <= '9':
            digit = ord(c) - ord('0')
        else:
            break
        value = value * 10 + digit
    return value

# 정수 -> 문자
def itoa(num):
    y = 0
    arr = []
    while num:
        y = num % 10
        num //= 10
        arr.append(chr(y + ord('0')))

    arr.reverse()
    str = "".join(arr)
    return str

x = '123'
y = 123
print(atoi(x))    
print(itoa(y))