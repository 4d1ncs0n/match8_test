import requests


def get_data(source:str) -> list:
    rawdata = requests.get(source).json()
    data = rawdata['values']
    return data

def find_target(target:int, point:int, data:list) -> object:
    player = data[point]
    
    if int(player['h_in']) == target:
        return ' '.join([player['first_name'], player['last_name']]), point
    
    if point == len(data)-1:
        return False, False
    
    point +=1
    
    return find_target(target, point, data)

def app(data:list, aim:int) -> None:
    i = 0
    final = len(data)-1
    check = list()
    while i <= final:
        da = data[i]
        target = aim-int(da['h_in'])
        couple, point = find_target(target, point=i, data=data)

        if point is False:
            i += 1
            check.append(False)
        
        elif i == point:
            i = point + 1
            check.append(False)

        else:
            player = ' '.join([da['first_name'], da['last_name']])
            print('\t'.join([player, couple]))
            i = point
            check.append(bool(couple))

    else:
        if any(check) is False:
            print('No matches found')


if __name__ == '__main__':

    source_data = 'https://mach-eight.uc.r.appspot.com/'
    data = get_data(source_data)

    aim = input('app ')
    app(data, int(aim))

