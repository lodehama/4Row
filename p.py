user_asset = 0
stock_list = {"삼성전자":250000,"SK하이닉스":1800000,"LG에너지솔루션":360000,"현대차":380000,"두산에너빌리티":90000}


class 매수 :
    def 보유주식에_추가() :
        user_stock = {}
        print('===== 현재가 =====')
        a = 0
        for i in stock_list :
            a += 1
            print(f'{a}) {i}: {stock_list[i]}원')
        while True :
            a = 0
            stock_name = input('어떤 주식을 구매할까요?')
            stock_number = input('몇 주 매수할까요?')
            for i in stock_list :
                try :
                    if a+1 == int(stock_name) :
                        print(f'{i} {stock_number}주 매수할게요.')
                        if i in user_stock :
                            user_stock[i] += int(stock_number)
                        else : user_stock[i] = int(stock_number)
                        break
                except ValueError :
                    print('잘못된 입력입니다. 다시 입력하세요.')
                    break
                a += 1
            question = input('더 구매할까요? 1) 예   2) 아니요 : ')    
            if question == '1' : continue
            elif question =='2' : break
        return user_stock

user_stock = 매수.보유주식에_추가()
print("보유 수량:",user_stock)
print(user_stock.get("삼성전자")) # 삼전수량
print(user_stock.get("SK하이닉스") == None) # 삼전수량