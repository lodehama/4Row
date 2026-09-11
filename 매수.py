class BuyStock:
    def __init__(self, wallet, money, stock_list, change_list, user_stock):
        self.wallet = wallet
        self.money = money
        self.stock_list = stock_list
        self.change_list = change_list
        self.user_stock = user_stock

    def buy(self) :
        total_buy = 0
        print("===== 현재가 =====")
        a = 0
        for i in self.stock_list :
            a += 1
            # print(f"{a}) {i}: {stock_list[i]:,}원 / 등락률: {change}%"")  # 이거 하면 마지막 거만 나옴
            print(f"{a}. {i}: {self.stock_list[i]:,}원 / 등락률: {self.change_list[i]}%")

        print(f"보유 주식: {self.user_stock}")

        while True:
            a = 0
            name = input("어떤 주식을 매수할까요?: ")
            quantity = input("몇 주 매수할까요?: ")
            for i in self.stock_list:
                if a+1 == int(name):

                    # 매수에 필요한 금액 계산
                    buy_price = self.stock_list[i] * int(quantity)

                    if buy_price > self.money:
                        print("보유 현금이 부족합니다.")
                        break
                    self.money -= buy_price      # 매수액만큼 현금 감소
                    total_buy += buy_price  # 총 매수액 계산
                    print(f"현금이 {self.money:,}원 남았습니다.")

                    try:
                        self.user_stock[i] += int(quantity)

                        break
                    except KeyError:
                        self.user_stock[i] = int(quantity)
                        break
                a += 1
            question = input("더 매수할까요? 1. 예 / 2. 아니요: ")    
            if question == "1": continue
            elif question == "2": 
                print(f"오늘 총 매수금액: {total_buy:,}")
                break
        self.save_stock()    # txt 파일에 저장
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