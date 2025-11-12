from inspect import iscoroutine

icecream = {'Tankboy': [1200, 5],
            'Pollapo': [1200, 7],
            'Ppangppare': [1800, 6],
            'Worldcorn': [1500, 3],
            'Melona': [1000, 10],
            'Heathunting': [1200, 4]}

print(f'Worldcorn의 희망가격: {icecream["Worldcorn"][0]}')
print(f'Worldcorn의 남은 수량: {icecream["Worldcorn"][1]}')

print('\n남은 수량이 7개 남은 제품 이름: ',end='')
for k, v in icecream.items():
    if v[1] == 7:
        print(k)

print('\n희망 가격이 1200원인 제품의 이름과 남은 수량 ')
print('*' * 50)
for k, v in icecream.items():
    if v[0] == 1200:
        print(f'제품명: {k}, 남은 수량: {v[1]}')

icecream['babamba'] = [700,20]
print('\n바밤바 추가 ')
print(icecream)