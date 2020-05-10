class Drawing:
    area = 100
    style = "North"
    __style2 = "China style"     #私有属性，私有变量
    def sleep(self):
        print("房子可以用来睡觉")
        print(self.__style2)
    def cook(self):
        print("房子还可以用来做饭")
    def __sleepat_bathroom(self):     #私有属性，私有方法
        print("我在厕所")
        self.sleep()
my_house = Drawing()
# my_house.__sleepat_bathroom()       #不能调用私有方法
my_house._Drawing__sleepat_bathroom()    #前面加上类名，可以调用
# print(my_house.__style2)             #不能调用私有变量
print(my_house._Drawing__style2)        #前面加上类名，可以调用
print(my_house.style)