rooms = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
room_info=[]
for room in rooms:
    room_num = ''
    i = 1
    while room[i] != ']':
        room_num += room[i]
        i += 1
    i += 1
    while i < len(room):
    room_info.append(int(room_num))
    print(room_info)
