class Game:
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power
    def fight(self,enemy_hp,enemy_power):
        final_hp = self.hp-enemy_power
        enemy_final_hp = enemy_hp-self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp == enemy_final_hp:
            print("平局")
        else:
            print("敌人赢了")
# game = Game(1000,200)
# game.fight(1000,150)

class HouYi(Game):
    def __init__(self):
        super().__init__(1000,150)
        self.defense = 100
    def defense1(self,enemy_hp,enemy_power):

        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print("后裔的血量是",self.hp)
            print("敌人的血量是",enemy_hp)
            if self.hp <= 0:
                print("敌人赢了")
                break
            elif enemy_hp <= 0:
                print("后裔赢了")
                break
houyi = HouYi()
houyi.defense1(1000,150)