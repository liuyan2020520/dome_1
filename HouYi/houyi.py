from Game.game import Game
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