list1=['a','v','d','d','g','g','y','e']
list1.reverse()
#list1.sort(reverse=1,key=str.lower)
print(list1)
#列表生成式
import random
lst=[random.randint(1,100) for a in range(10)]
lst2=[item**item for item in range(0,10) if item**item<100000]
print(lst2)

lst3=[
    [1,2,3,4,'as',6,6],
    [324,24,5,6,131,44]
]
for row in lst3:
    for item in row:
        print(item,end='\t')
    print()

lst4=[[j for j in range(0,10)] for i in range(0,10)]
print(lst4)