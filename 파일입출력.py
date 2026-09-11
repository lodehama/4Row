import random
import csv
da = {'kiwoom':'2001',"digital":"1234","academy":"2024"} # da: 로그인 데이터

class errors :
    def wrong() :
        print('')
        print('잘못 입력되었습니다. 다시 입력해 주세요.')
    def no() :
        print('')
        print('아무것도 저장되지 않았습니다.')

class games :
    class lotto :
        def lotto_auto(self, bo) :
            while len(bo) < 6 :
                ra = random.randint(1,45) # ra: 생성 번호
                if (ra in bo) :
                    continue
                else :
                    bo.append(ra)
            return bo
        def lotto_manual(self, bo) :
            while len(bo) < 6 :
                print('')
                try :
                    ra = int(input(f'{len(bo)+1}번째 번호를 입력하세요. ')) # ra: 생성 번호
                    if (ra in bo) :
                        print('')
                        print('동일한 번호는 입력할 수 없습니다.')
                    elif ra > 45 or ra < 1 :
                        print('')
                        print('1부터 45 사이의 숫자를 입력하세요.')
                    else :
                        bo.append(ra)
                except ValueError : errors.wrong()
            return bo
        def lotto_main_menu(self) : # lotto: 로또 번호 생성
            save_data_inst = save_data()
            while True :
                print('')
                print('로또 번호 생성기입니다. 선택해주세요.')
                lm = input('1) 자동추첨   2) 수동추첨   3) 메뉴로 돌아가기 : ') # lm: 로또 메뉴
                bo = [] # bo: 선택된 숫자들
                if lm == '1' : 
                    bo = self.lotto_auto(bo)
                elif lm == '2' :
                    bo = self.lotto_manual(bo)
                elif lm == '3' :
                    break
                else :
                    errors.wrong()
                    continue
                save_data_inst.lotto_saving(bo)
    class upanddown :
        def upanddown(self, di) :
            ra = random.randint(1,int(di)*200-100) # ra: 생성 번호
            print(ra,'')
            print('게임 스타트! 숫자를 정했습니다.')
            nu = int(input('최대한 빠르게 맞춰보세요.: ')) # nu: 선택한 번호
            co = 0 # c = 시도횟수
            while True :
                try :
                    co += 1
                    if ra > nu :
                        print(f'{nu}보다 높은 숫자입니다.')
                        nu = int(input('다시 맞춰보세요. '))
                    elif ra < nu :
                        print(f'{nu}보다 낮은 숫자입니다.')
                        nu = int(input('다시 맞춰보세요. '))
                    else :
                        print('')
                        print(f'정답입니다~! {co}번 시도하셨습니다!')
                        break
                except ValueError :
                    errors.wrong()
            return co
        def upanddown_main_manu(self) :
            while True :
                print('')
                print('난이도를 선택하세요.')
                di = input('1) 쉬움(1~100)   2) 중간(1~300)   3) 어려움(1~500)   4) 메뉴로 돌아가기 : ') # di: 난이도
                if di == '1' or di == '2' or di == '3' :
                    co = self.upanddown(di)
                    save_data.upanddown_saving(co)
                if di == 4 : break
                else : errors.wrong()
    def games_main_menu() :
        games_lotto = games.lotto()
        games_upanddown = games.upanddown()
        while True:
            print('')
            print('어떤 게임을 실행할까요?')
            ga = input('1) 로또 번호   2) 업 앤 다운    3) 행 맨 : ') # ga: 게임 선택
            if ga == '1' : games_lotto.lotto_main_menu()
            elif ga == '2' : games_upanddown.upanddown_main_manu()
            elif ga == '3' : 행맨아직추가안함()
            else :
                errors.wrong()
                continue
            break

class save_data :
    def lotto_saving(self, bo) :
        bo.sort(reverse=False)
        print('')
        print('두근두근')
        print(bo[0], bo[1], bo[2], bo[3], bo[4], bo[5])
        print('생성되었습니다. 이력에 저장합니다.')
        with open("lotto.txt","a",encoding="utf-8")as fi:
	        fi.write(str(bo)+'\n')
    def lotto_saved() :
        with open("lotto.txt","r",encoding="utf-8")as fi:
            ct = fi.read() # ct: 기록 불러오기
            if ct == "" : errors.no()
            else : 
                print('')
                print(ct)
    def upanddown_saving(co) :                
        while True :
            ra = input('랭킹에 저장할까요? 1) 예   2) 아니요: ')
            if ra == '1' :
                print('')
                ni = input('닉네임을 입력해 주세요.: ')
                with open("upanddown.csv","a",encoding="utf-8-sig", newline="")as fi:
                    wr = csv.writer(fi)
                    wr.writerow([ni,co])
                print('저장되었습니다.')
                break
            elif ra == '2': break
            else : print('잘못 입력되었습니다. 다시 입력해 주세요.')
    def upanddown_saved() :
        with open("upanddown.csv","r",encoding="utf-8-sig")as fi:
            rd = list(csv.reader(fi)) # rd: 리더
            RR = []
            for rw in rd:
                if len(rw) >= 2:
                    name = rw[0]
                    score = int(rw[1])
                    RR.append((score, name))
                if not RR : errors.no()
                RR.sort()
                c = 1
                print('')
                for i in range(len(RR)) :
                    x, y = RR[i]
                    if i > 0 and x != RR[i-1][0]:
                        c = i+1
                    print(f'{c}등: {y} - {x}번')


def login() :
    for i in range (3) :
        ok = 0 # ok: 성공 여부
        print('')
        id = input("아이디를 입력하세요.").lower()
        pw = input("비밀번호를 입력하세요.")
        if id in da :
            if da[id] == pw :
                ok = 1
                break
            elif i != 2 :
                errors.wrong()
                print(f"주의하세요. {2-i}회 더 실패할 경우, 강제 종료됩니다.")
        elif i !=2 :
            errors.wrong()
            print(f"주의하세요. {2-i}회 더 실패할 경우, 강제 종료됩니다.")
    return ok, id
def main_menu() :
    while True:
        print('')
        print('원하시는 메뉴를 선택해주세요.')
        mo = input('1) 게임 시작   2) 게임 이력   3) 게임 종료 : ') # mo: 모드 선택
        if mo == '1' : games.games_main_menu()
        elif mo == '2' :
            print('')
            ra = int(input('어떤 이력을 불러올까요? 1) 로또 이력   2) 업앤다운 랭킹 : ')) # ra: 어떤 랭킹인지
            if ra == 1 :
                save_data.lotto_saved()
            if ra == 2 :
                save_data.upanddown_saved()
        elif mo == '3' :
            print('')
            print('종료되었습니다.')
            break
        else :
            errors.wrong()

ok, id = login()
if ok == 1 :
    print('')
    print('로그인에 성공하였습니다.')
    print(f'안녕하세요, {id}님.')
    main_menu()
if ok == 0 :
    print('')
    print('종료되었습니다.')