import tkinter as tk
from tkinter import messagebox

class Coffee:
    def __init__(self):
        # 자판기 초기 상태
        self.total_amount = 10             # 자판기 내 커피 개수
        self.total_amount_price = 5000     # 자판기 보유 금액
        self.coffee_price = 300            # 커피 한 잔 가격

    # 커피 구매 로직
    def get(self, put_price, req_coffee_nums):
        total_cost = self.coffee_price * req_coffee_nums

        # 자판기에 커피가 부족한 경우
        if req_coffee_nums > self.total_amount:
            return f"⚠️ 자판기에 커피가 부족합니다.\n반환 금액: {put_price}원"

        # 돈이 충분한 경우
        if put_price >= total_cost:
            remaining_price = put_price - total_cost
            self.total_amount -= req_coffee_nums
            self.total_amount_price += total_cost
            result = f"☕ 커피 {req_coffee_nums}개 나왔습니다."
            if remaining_price > 0:
                result += f"\n거스름돈 {remaining_price}원을 반환합니다."
            else:
                result += "\n거스름돈이 없습니다."
            return result

        # 일부만 넣은 경우 (한 잔 이상 살 수 있으나 총액은 부족)
        elif put_price >= self.coffee_price:
            can_buy = put_price // self.coffee_price
            if can_buy > self.total_amount:
                can_buy = self.total_amount
            remaining_price = put_price - (self.coffee_price * can_buy)
            self.total_amount -= can_buy
            self.total_amount_price += (self.coffee_price * can_buy)
            result = f"☕ 요청한 개수보다 적지만 {can_buy}개의 커피를 제공합니다."
            if remaining_price > 0:
                result += f"\n거스름돈 {remaining_price}원을 반환합니다."
            return result

        # 돈이 부족한 경우
        else:
            return f"⚠️ 돈이 부족하여 커피를 제공할 수 없습니다.\n반환 금액: {put_price}원"

    # 메뉴판 정보 출력용 텍스트
    def info_text(self):
        return (
            "====== ☕ 커피 자판기 메뉴 ======\n"
            f"남은 커피 개수 : {self.total_amount}개\n"
            f"자판기 보유 금액 : {self.total_amount_price}원\n"
            f"커피 한 잔 가격 : {self.coffee_price}원\n"
            "================================"
        )


# GUI 클래스
class CoffeeMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("☕ 커피 자판기")

        # 커피 자판기 객체 생성
        self.machine = Coffee()

        # 메뉴판 라벨
        self.info_label = tk.Label(root, text=self.machine.info_text(), font=("맑은 고딕", 11), justify="left")
        self.info_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # 입력 영역
        tk.Label(root, text="돈을 넣어주세요(원):", font=("맑은 고딕", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.money_entry = tk.Entry(root, width=10)
        self.money_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="원하는 커피 개수:", font=("맑은 고딕", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.count_entry = tk.Entry(root, width=10)
        self.count_entry.grid(row=2, column=1, padx=5, pady=5)

        # 버튼
        self.buy_button = tk.Button(root, text="커피 구매하기", command=self.buy_coffee, font=("맑은 고딕", 10, "bold"))
        self.buy_button.grid(row=3, column=0, columnspan=2, pady=10)

        # 결과 출력 영역
        self.result_label = tk.Label(root, text="", font=("맑은 고딕", 10), justify="left", fg="blue")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def buy_coffee(self):
        try:
            put_price = int(self.money_entry.get())
            req_coffee_nums = int(self.count_entry.get())
        except ValueError:
            messagebox.showerror("입력 오류", "⚠️ 숫자만 입력해주세요!")
            return

        result = self.machine.get(put_price, req_coffee_nums)

        # 결과 표시
        self.result_label.config(text=result)

        # 메뉴판 갱신 (커피 개수나 자판기 금액이 바뀜)
        self.info_label.config(text=self.machine.info_text())

        # 입력창 초기화
        self.money_entry.delete(0, tk.END)
        self.count_entry.delete(0, tk.END)


# 프로그램 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeMachineApp(root)
    root.mainloop()
