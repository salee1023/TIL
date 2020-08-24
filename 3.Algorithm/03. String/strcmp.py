def strcmp(str1, str2):
    ans = True
    if len(str1) != len(str2):
        ans = False
    else:
        i = 0
        while i < len(str1):
            if str1[i] != str2[i]:
                ans = False
                break
            else:
                i += 1
                continue
    return ans

# --------------------------
str1 = 'hello'
str2 = 'hello'
a = strcmp(str1, str2)
print(a)

