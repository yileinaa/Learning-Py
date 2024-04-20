x ='dasdasdasdasd'
y=x.index('s')
z=x.count('s')
print(y,z)
lst=list(range(1,10,2))
print(lst)
#del(lst)
for item in lst:
    print(item)
for index,item in enumerate(lst,start=1):
    print(index,item)