import json

def rotate(data):
    # 변수 설정
    am_list = []
    pm_list = []
    temp_dict ={}

    # 각 리스트에 오전 체온과 오후 체온을 넣어준다
    for day in data:
        am_list.append(day[0])
        pm_list.append(day[1])
    
    # 오전 체온 리스트와 오후 체온 리스트를 딕셔너리에 넣어준다
    temp_dict['am'] = am_list
    temp_dict['pm'] = pm_list
    
    # 딕셔너리를 return 
    return temp_dict 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(rotate(temperature_list))
    # => {
    #     'am': [36.7, 36.9, 37.8, 36.7, 36.3, 36.5, 36.8], 
    #     'pm': [36.5, 37.5, 37.8, 36.5, 36.4, 36.5, 36.6]
    # }
