class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? : "))
        if(order > chicken):
            print("재료가 부족합니다")
        elif(0 < order <= chicken):
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting +=1
            chicken -= order
        else:
            raise ValueError

        if(chicken <= 0):
            break

    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
    except SoldOutError as err:
        print(err)

print("재료 소진")
