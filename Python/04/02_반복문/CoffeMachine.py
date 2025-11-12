# 커피머신 프로그램

coffee = 5        # 커피 개수
price = 300       # 커피 한 잔 가격

print("=== 커피머신을 시작합니다 ===")

while True:
    print(f"\n남은 커피 개수: {coffee}개")

    # 커피가 다 떨어졌을 경우 종료
    if coffee == 0:
        print("커피가 모두 소진되었습니다. 판매를 종료합니다.")
        break

    # 사용자 입력
    money = int(input("돈을 넣어주세요 (원): "))

    # 돈이 충분한 경우
    if money >= price:
        coffee -= 1
        change = money - price
        print("커피를 제공합니다 ☕")
        print(f"거스름돈: {change}원")
        print(f"남은 커피 개수: {coffee}개")
    else:
        # 돈이 부족한 경우
        print("돈이 부족합니다. 커피를 제공할 수 없습니다.")
        print(f"거스름돈: {money}원")

print("\n=== 프로그램 종료 ===")
