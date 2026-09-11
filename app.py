from 매수 import BuyStock
from 매도 import SellStock
from 등락 import ChangePrice

class App:
    def __init__(self):
        self.wallet = 10000000   # 초기 자산
        self.money = 10000000    # 현금
        self.stock_list = {"삼성전자":250000,"SK하이닉스":1800000,"LG에너지솔루션":360000,"현대차":380000,"두산에너빌리티":90000}
        self.change_list = {}
        self.user_stock = {}
        # self.b = BuyStock(self.wallet, self.money, self.stock_list, self.change_list, self.user_stock)
        # self.s = SellStock(self.wallet, self.money, self.stock_list, self.change_list, self.user_stock)
        self.c = ChangePrice(self.stock_list, self.change_list)

    def run(self):
        # 첫 날엔 주식 가격 건드리지 않고 시작
        for name in self.stock_list:
            self.change_list[name] = 0

        try:
            file = open("stock_info.txt","r",encoding="utf-8")

            for line in file:
                name, quantity = line.strip().split(",")

                # 돈 불러오기
                if name == "wallet":
                    self.wallet = int(quantity)

                elif name == "money":
                    self.money = int(quantity)

                # 주식 불러오기
                else:
                    self.user_stock[name] = int(quantity)

            file.close()

        except FileNotFoundError:
            # print("아직 저장된 주식이 없습니다.")
            pass

        while True:
            menu = input("1. 매수 / 2. 매도 / 3. 내일로 이동 / 4. 종료: ")

            if menu == "1":
                self.b = BuyStock(self.wallet, self.money, self.stock_list, self.change_list, self.user_stock)
                self.user_stock, self.money = self.b.buy()
                print("보유 주식:",self.user_stock)

            elif menu == "2":
                self.s = SellStock(self.wallet, self.money, self.stock_list, self.change_list, self.user_stock)
                self.user_stock, self.money = self.s.sell()
                print("보유 주식:",self.user_stock)

            elif menu == "3":
                self.c.change_stock_price()
                print("============================")
                print("날짜가 변경되었습니다.")

                stock_value = 0

                for name in self.user_stock:
                    stock_value += self.stock_list[name] * self.user_stock[name]

                print(f"보유 현금: {self.money:,}원")
                print(f"보유 주식 가치: {stock_value:,}원")
                print(f"전재산: {stock_value + self.money:,}원")
                print("============================")

                a = 0
                for i in self.stock_list:
                    a += 1
                    print(f"{a}) {i}: {self.stock_list[i]:,}원 / 등락률: {self.change_list[i]}%")

            elif menu == "4":
                print("종료합니다.")
                break

            else:
                print("1~4 중에서 입력해주세요.")