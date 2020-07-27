def swap(word):
    # 대소문자는 32만큼 차이난다 
    new_word = ""
    for letter in word:
        # 대문자 -> 소문자
        if (ord(letter)) <= 90:
            new_word += chr(ord(letter) + 32)  
        # 소문자  -> 대문자  
        else:    
            new_word += chr(ord(letter) - 32)
    return new_word

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(swap('aPpLe'))
    # => 'ApPlE'
    print(swap('SSAFY'))
    # => 'ssafy'
    print(swap('Python'))
    # => 'pYTHON'