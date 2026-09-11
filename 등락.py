import random

class ChangePrice():
    def __init__(self, stock_list, change_list):
        self.stock_list = stock_list
        self.change_list = change_list

    # 매일 주식의 가격 변동
    def change_stock_price(self):
        for name in self.stock_list:
            change = random.randint(-30, 30)    # 하루에 +-30%까지 가능
            self.change_list[name] = change          # 이거 안 쓰면 등락률이 마지막 시행으로 일괄 출력됨
            self.stock_list[name] = int(self.stock_list[name] * (1 + change / 100))