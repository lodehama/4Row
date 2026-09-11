
class SellStock():
    def __init__(self, user_stock):
        self.user_stock = user_stock # 구매 가능 주식 리스트

    def sell(self):
        print(f"보유 주식: {self.user_stock}")
        while True:
            name = input("매도할 주식을 입력해주세요: ")
            if name in user_stock:
                while True:
                    quantity = input("매도 수량을 입력해주세요: ")
                    try:
                        if int(quantity) <= user_stock[name]:
                            self.user_stock[name] -= int(quantity)
                            break
                        print("보유한 수량보다 더 많이 매도할 수 없습니다.")
                    except ValueError:
                        print("매도 수량을 정확히 입력해 주세요.")  
                break
            else:
                print("보유하지 않은 주식입니다.")  
        print(f"{name} {quantity}주를 매도했습니다.")
        print(f"보유 주식: {self.user_stock}")      

user_stock = {"삼성전자":10, "하이닉스": 5} # 보유 주식
s = SellStock(user_stock)

s.sell()