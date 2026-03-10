# 作者：扬帆
# 2026年03月09日13时54分07秒
# 739368408@qq.com
class Animal:
    def __init__(self, name): self.name = name
    def eat(self): print("吃---")
    def run(self): print("跑---")
class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name) # 子类对象调用父亲的 init super后面要加（）表示对象指定
        self.color = color
    def bark(self): print('汪汪叫')
if __name__ == '__main__':
    dog = Dog('大黄', '黄色')
    print(dog.name)
    print(dog.color)
    dog.bark()