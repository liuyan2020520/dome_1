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
        final_hp = self.hp + self.defense - enemy_power
        enemy_final_hp = enemy_hp -self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp == enemy_final_hp:
            print("平局")
        else:
            print("敌人赢了")
        # print("我赢了") if final_hp > enemy_final_hp else print("敌人赢了")    #三目运算

houyi = HouYi()
houyi.defense1(1000,150)