# 作者: 王道 龙哥
# 2024年12月27日15时41分27秒
# xxx@qq.com

a = 2
b = 2
print(a is b)
a = 'hello'
print(id(a))
del a
b = 'hello'
print(id(b))
c=[1,2,3]
d=[1,2,3]
print(id(c),id(d),sep='\n')




