class SellStock:
    def __init__(self, wallet, money, stock_list, change_list, user_stock):
        self.wallet = wallet
        self.money = money
        self.stock_list = stock_list
        self.change_list = change_list
        self.user_stock = user_stock

    def sell(self):
        total_sell = 0
        print(self.money)

        while True:
            name = input("매도할 주식을 입력해주세요: ")
            if name in self.user_stock:
                while True:
                    quantity = input("매도 수량을 입력해주세요: ")
                    try:
                        if int(quantity) <= self.user_stock[name]:

                            price = self.stock_list[name]            # 이름으로 입력
                            sell_price = price * int(quantity)  # 총 매도금액

                            self.user_stock[name] -= int(quantity)
                            self.money += sell_price         # 매도액만큼 현금 증가
                            total_sell += sell_price    # 총 매도액 계산

                            print(f"오늘 총 매도금액: {total_sell:,}")
                            break

                        print("보유한 수량보다 더 많이 매도할 수 없습니다.")
                    except ValueError:
                        print("매도 수량을 정확히 입력해 주세요.")  
                break
            else:
                print("보유하지 않은 주식입니다.")
        print(f"{name} {quantity}주를 매도했습니다.")

        self.save_stock()    # txt 파일에 저장

        print(f"지금까지 사용한 금액 : {self.wallet-self.money:,}")   # 이거 보유 주식의 총액(가치가) 아니고 순매수 금액임. 처음 샀을 떄 들어간 원금
        print(f"보유 현금 : {self.money:,}")

        return self.user_stock, self.money

    # 메모장에 보유 주식 저장
    def save_stock(self):
        file = open("stock_info.txt","w",encoding="utf-8")

        # 돈 저장
        file.write(f"wallet, {self.wallet}\n")
        file.write(f"money, {self.money}\n")

        for name in self.user_stock:
            file.write(f"{name}, {self.user_stock[name]}\n")

        file.close()