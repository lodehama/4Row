wallet = 10000000   # 초기 자산
money = 10000000    # 현금
stock_list = {"삼성전자":250000,"SK하이닉스":1800000,"LG에너지솔루션":360000,"현대차":380000,"두산에너빌리티":90000}


# 메모장에서 보유 주식 호출
user_stock = {}
try:
    file = open("stock_info.txt","r",encoding="utf-8")

    for line in file:
        name, quantity = line.strip().split(",")

        # 돈 불러오기
        if name == "wallet":
            wallet = int(quantity)

        elif name == "money":
            money = int(quantity)

        # 주식 불러오기
        else:
            user_stock[name] = int(quantity)

    file.close()

except FileNotFoundError:
    pass

# 메모장에 보유 주식 저장
def save_stock():
    file = open("stock_info.txt","w",encoding="utf-8")

    # 돈 저장
    file.write(f"wallet, {wallet}\n")
    file.write(f"money, {money}\n")

    for name in user_stock:
        file.write(f"{name}, {user_stock[name]}\n")

    file.close()

# 매수
class 매수 :
    def 보유주식에_추가() :
        global money
        total_buy = 0
        print('===== 현재가 =====')
        a = 0
        for i in stock_list :
            a += 1
            print(f'{a}) {i}: {stock_list[i]:,}원')
        while True :
            a = 0
            stock_name = input('어떤 주식을 구매할까요?')
            stock_number = input('몇 주 매수할까요?')
            for i in stock_list :
                if a+1 == int(stock_name) :
                    print(f'{i} {stock_number}주 매수할게요.')

                    ## 매수에 필요한 금액 계산 ##
                    buy_price = stock_list[i] * int(stock_number)

                    if buy_price > money:
                        print("보유 현금이 부족합니다.")
                        break
                    money -= buy_price      # 매수액만큼 현금 감소
                    total_buy += buy_price  # 총 매수액 계산
                    print(f"현금이 {money:,}원 남았습니다.")

                    try :
                        user_stock[i] += int(stock_number)

                        break
                    except KeyError :
                        user_stock[i] = int(stock_number)
                        break
                a += 1
            question = input('더 구매할까요? 1) 예   2) 아니요 : ')    
            if question == '1' : continue
            elif question =='2' : 
                print(f"오늘 총 매수금액: {total_buy:,}")
                break
        save_stock()    # txt 파일에 저장
        return user_stock
user_stock = 매수.보유주식에_추가()
print("보유 수량:",user_stock)

# 매도
class SellStock():
    def __init__(self, user_stock):
        self.user_stock = user_stock # 구매 가능 주식 리스트

    def sell(self):
        global money
        total_sell = 0

        while True:
            name = input("매도할 주식을 입력해주세요: ")
            if name in user_stock:
                while True:
                    quantity = input("매도 수량을 입력해주세요: ")
                    try:
                        if int(quantity) <= user_stock[name]:

                            price = stock_list[name]            # 이름으로 입력
                            sell_price = price * int(quantity)  # 총 매도금액

                            self.user_stock[name] -= int(quantity)
                            money += sell_price         # 매도액만큼 현금 증가
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
        print(f"보유 주식: {self.user_stock}")

        save_stock()    # txt 파일에 저장

        print(f"보유 주식 가치 : {wallet-money:,}")
        print(f"보유 현금 : {money:,}")
        # print(f"총 자산 : ")
    
s = SellStock(user_stock)
s.sell()