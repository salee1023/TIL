import json

def over(movie):
    # 평점이 8점 이상인지 확인 후, 넘으면 True반환
    if movie['user_rating'] >= 8:
        return True
    # 넘지 않으면 False 반환
    else:
        return False    
    pass

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # => True