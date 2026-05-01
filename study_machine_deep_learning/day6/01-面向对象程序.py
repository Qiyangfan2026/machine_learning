# 作者：扬帆
# 2026年03月07日22时31分04秒
# 739368408@qq.com
class Cat:
    def __init__(self, cat_name, cat_color,cat_weight):
        self.name = cat_name
        self.color = cat_color
        self.weight = cat_weight
    def drink(self):
        print("%s在喝水"%(self.name))

    def eat(self):
        print(f"{self.name}爱吃鱼")

tom = Cat('laze_cat','red','5kg')
tom.drink()
tom.eat()
print(tom.color)
