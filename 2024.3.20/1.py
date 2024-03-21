import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))#保留字区分大小写
x ='3.14+3'
print(x,type(x))
y=eval(x)
print(y,type(y))
h='sadasdasd'
for i in range(0,len(h)):
    print(h[i],len(h))
h1=h[0:8:2]#切片负数逆序输出
print(h1)