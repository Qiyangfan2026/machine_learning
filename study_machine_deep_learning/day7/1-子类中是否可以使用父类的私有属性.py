# 作者: 王道 龙哥
# 2024年12月31日09时15分18秒
# xxx@qq.com

class A:
    def __init__(self):
        self.__age = 18
        self.name="dog"

    def base_age(self):
        print(self.__age)

class B(A):
    # def __init__(self):
    #     super().__init__()
    def get_age(self):
        print(self.__age)
        self.base_age()


if __name__ == '__main__':
    zhangsan = B()
    zhangsan.get_age()
    print(zhangsan.namename)