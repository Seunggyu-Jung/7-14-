from random import*

class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):   # 일반 유닛들도 데미지를 받을 수 있기 때문
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}이 파괴되었습니다.".format(self.name))


class attackunit(unit): # 상속받을 클래스에 괄호를 치고 상속받을 클래스를 작성한다.
    def __init__(self, name, hp, speed, damage):
        unit.__init__(self, name, hp, speed)   # 상속받은 클래스.__init__(self, 상속 받을 멤버변수)
        self.damage = damage
       

    def attack(self, location):
        print("{0} 유닛 : {1}방향으로 공격합니다.[공격력 {2}]".format(self.name, location, self.damage))


class flyable:
     def __init__(self, flying_speed):
        self.flying_speed = flying_speed

     def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

class flyableattackunit(attackunit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attackunit.__init__(self, name, hp, 0, damage)  #지상 speed = 0
        flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

class Marin(attackunit):
    def __init__(self):
        attackunit.__init__(self, "마린", 40, 1, 5)  # 상속받는 함수를 초기화시킨것

    def stimpack(self):   #스팀팩 사용
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀책을 사용합니다. (HP 10 감소)".format(self.name))

        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(attackunit):

    seize_developed = False
    
    def __init__(self):
        attackunit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False   #멤버 변수 설정

    def set_seize_mode(self):      # 시즈모드를 처음 만듦 -> 실행하진 않음
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:         # 시즈모드를 하고 싶을때
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode == True

        else:                               # 시즈모드를 풀고 싶을때
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode == False
        
class Wrath(flyableattackunit):
    def __init__(self):
        flyableattackunit.__init__(self, "레이스", 80 , 20 ,5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹을 해제합니다.".format(self.name))
            self.clocked == False

        else:
            print("{0} : 클로킹을 설정합니다.".format(self.name))
            self.clocked == True

def game_start():
    print("[알림] : 새로운 게임을 시작합니다.")

def game_over():
    print("Player : GG")
    print("[알림] : Player가 게임에서 퇴장했습니다.")

# 게임시작
game_start()


m1 = Marin()
m2 = Marin()
m3 = Marin()
t1 = Tank()
t2 = Tank()
w1 = Wrath()

# 유닛 일괄 관리 (유닛을 한번에 관리 -> 리스트를 만들어 해결 + append 처리)

attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

# 전군 이동 -> for 사용
for Unit in attack_unit:
    Unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드가 개발 되었습니다.")

# 공격모드 준비(마린-> 스팀팩, 탱크 -> 시즈, 레이스 -> 클로킹)
for Unit in attack_unit:
    if isinstance(Unit ,Marin): # 해당 클래스의 객체인지 판별해주는 함수
        Unit.stimpack()

    elif isinstance(Unit ,Tank):
        Unit.set_seize_mode()

    elif isinstance(Unit ,Wrath):
        Unit.clocking()

#전군 공격 
for Unit in attack_unit:
    Unit.attack("1시")

# 데미지를 입음
for Unit in attack_unit:
    Unit.damaged(randint(5,20)) # 공격은 렌덤으로 받음

# 게임 종료
game_over()

