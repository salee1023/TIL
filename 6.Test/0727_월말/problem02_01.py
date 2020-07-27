import json

def check(data):
    count = 0
    for day_data in data:
        for single_data in day_data:
            #37.5 이상이면 count + 1
            if single_data >= 37.5:
                count += 1
                # 연속 3일 37.5이상이면 True 반환
                if count == 3:
                    return True   
                    break
            #37.5 미만이면 count - 1         
            else:
                #단, count는 음수가 될 수 없다
                while count > 0:
                    count -= 1    
    else:
        return False
                  
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True