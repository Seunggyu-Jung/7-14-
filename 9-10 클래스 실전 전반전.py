class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
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
        print("{0} 유닛 : {1}방향으로 공격합니다.".format(self.name, location))


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
        print("[공중 유닛 이동]")
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
    



