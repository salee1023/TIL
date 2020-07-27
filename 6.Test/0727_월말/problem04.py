def dec_to_bin(n):
    # 더 이상 나누어지지 않으면 1을 반환
    if n == 1:
        return '1' 
    # 2로 나눌 때마다 새로 함수 호출
    else:
        if n % 2 == 1:
            bin_str =  '1'
        else:
            bin_str = '0'        
        return dec_to_bin(n//2) + bin_str


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'
    print(dec_to_bin(2))
    print(dec_to_bin(1))