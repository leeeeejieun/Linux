class Fridge:
    isOpend = False
    foods = []

    # 냉장고 문 열기
    def open(self):
        self.isOpened = True
        print('[ INFO ] 냉장고 문이 열렸습니다.')

    # 냉장고에 음식 넣기
    def put(self, food):
        if self.isOpened:
            self.foods.append(food)
            print(f'[ INFO ] 냉장고 안에 {self.foods}을 넣었습니다.')
        else:
            print('[ INFO ] 냉장고 문이 문이 닫혀있습니다.')

    # 냉장고 문 닫기
    def close(self):
        self.isOpened = False
        print('[ INFO ] 냉장고 문을 닫았습니다.')

class Food:
    pass