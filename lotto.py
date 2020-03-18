import random


class LottoBall:  # 번호가 써있는 로또 공이 만들어 지는 클래스
    def __init__(self, num):
        self.num = num


class LottoSelect:
    def __init__(self):  # 로또 공 모집단을 만드는 생성자
        self.ballList = []
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))

    def selectBalls(self):  # 모집단을 섞은 뒤 앞에서부터 6개 고르는 함수
        random.shuffle(self.ballList)
        return self.ballList[0:6]


class LottoUI:
    def __init__(self):
        self.machine = LottoSelect()

    def playLotto(self):
        print("로또뽑는다잉")
        selectBalls = self.machine.selectBalls()
        for i in selectBalls:
            print(i.num)


go = LottoUI()
go.playLotto()
