def caesar(word, n):
    new_word = ""
    for letter in word:
        # 대문자
        if (ord(letter)) <= 90:
            # 범위를 넘어가면 다시 처음으로 되돌려줌
            if (ord(letter) + n) > 90:
                new_word += chr(ord(letter) + n -26)    
            else:    
                new_word += chr(ord(letter) + n)
        
        # 소문자        
        else:
            if (ord(letter) + n) > 122:
                new_word += chr(ord(letter) + n -26)    
            else:    
                new_word += chr(ord(letter) + n)    
                      
    return new_word

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # => 'fuuqj'
    print(caesar('ssafy', 1))
    # => 'ttbgz'
    print(caesar('Python', 10))
    # => 'Zidryx'