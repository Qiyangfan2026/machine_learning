# 作者：扬帆
# 2026年03月09日14时07分47秒
# 739368408@qq.com
class Dog(object):
    def __init__(self, name):
        self.name = name
    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)
class XiaoTianDog(Dog):
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)
class Person(object):
    def __init__(self, name):
        self.name = name
    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
# 让狗玩耍
        dog.game()
# 1. 创建一个狗对象

if __name__ == '__main__':
    wangcai = Dog("旺财")
    #wangcai = XiaoTianDog("飞天旺财")
    # 2. 创建一个大象对象
    xiaoming = Person("大象")
    num=input()
    my_list=num.split()#只能针对str分割
    int_list = list(map(int, my_list))#类型转换
    print(my_list)
    print(int_list)