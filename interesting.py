#--------------------------------------------------------------
#将x,y的次数从20到25依次尝试 会发生神奇的事情
#--------------------------------------------------------------
x=1.145121279e23
y=1.145121272e23
print(x,y)
print('{:.50e}'.format((x+y)*(x-y)))
print('{:.50e}'.format(x**2-y**2))
a=1145121279000
b=1145121272000
print((a+b)*(a-b))