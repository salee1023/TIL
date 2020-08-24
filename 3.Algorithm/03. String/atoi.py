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

a = '123'
b = atoi(a)
print(b)