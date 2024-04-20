#元组，不可变序列
t=("hello",[10,23,213],"python","world")
print(t)
#tuple函数创建
t2=tuple([10,20,30])
#del t2
print(t2)
for i in range(len(t)):
    print(t[i])
#print(t.__next__())#提取元素
for index,item in enumerate(t,start=0):
    print(index,item)

#字典
di={1:'a',2:'b',3:'c',4:'d',5:'e'}
keys=tuple(di.keys())
print(keys)
print(di.get(1,'不存在'))
li1=(1,2,3,4,5,6)
li2=('a','b','c','d','e','f')
zipped=zip(li1,li2)
print(list(zipped))
d=dict(t=1,p=2,zhen=3,shuai=4)
print(d)

#字典生成式
import random
d={item:random.randint(1,100)for item in range(4)}

lis1=(1,2,3,4,5,6)
lis2=('a','b','c','d','e','f')
da={key:value for (key,value) in zip(lis1,lis2)}
