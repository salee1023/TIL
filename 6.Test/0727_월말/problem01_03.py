import json

def history(movie):
    # 줄거리에 ' 과거'가 있으면 True 반환
    if '과거' in  movie['overview']:
        return True
    # 없다면 False 반환
    else:
        return False    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # => False