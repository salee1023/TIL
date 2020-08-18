import requests
import random
from django.shortcuts import render

# Create your views here.
def lotto(request):
    #로또 정보 가져오기
    r = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=924')
    lotto_dict = r.json()
    lotto_list = []
    for i in range(1,7):
        lotto_list.append(lotto_dict[f'drwtNo{i}'])
    
    bonusnum = lotto_dict.get('bnusNo')
    
    # 랜덤으로 생성한 숫자 중에서 당첨 횟수 알아보기.
    money = [0]*6
    for _ in range(10000):
        mylotto = random.sample(range(1,46),6)
        count = 0
        # 일치하는 숫자 개수 세기
        for m in mylotto:
            if m in lotto_list:
                count += 1
        if count == 6:
            money[0] += 1
        elif count == 5:
            if bonusnum in mylotto:
                money[1] += 1
            else:
                money[2] += 1
        elif count == 4:
            money[3] += 1
        elif count == 3:
            money[4] += 1
        else:
            money[5] += 1                        

    context = {
        'lottolist' : lotto_list,
        'bonusnum' : bonusnum,
        'money' : money
    }

    return render(request, 'pages/lotto.html', context)

def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people' : people
    }
    return render(request, 'pages/dinner.html', context)    

