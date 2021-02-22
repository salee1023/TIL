import requests
import json

def  getCountries(debts):
    answer = []
    # people = []
    peoples = {}

    for info in debts:
        if info[0] in peoples:
            peoples[info[0]] -= int(info[2])
        if info[0] not in peoples:
            peoples[info[0]] = -int(info[2])
        if info[1] in peoples:
            peoples[info[1]] += int(info[2])
        if info[1] not in peoples:
            peoples[info[1]] = int(info[2])

    reverse_dict = dict(map(reversed, peoples.items()))
    reverse_dict[min(reverse_dict.keys())]
    print(reverse_dict)


print(getCountries([['Alex', 'Blake', '5'], ['Blake', 'Alex', '3'], ['Casey', 'Alex', '7'],['Casey', 'Alex', '4'], ['Casey', 'Alex', '2']]))
