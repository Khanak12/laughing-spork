x=[1,2,3,5]
y=[100,200,300,500]
ans=zip(x,y)
print(list(ans))

x1=[1,2,3,4]

def h(number):
    return number*number

square=list(map(h,x1))
print(square)

for i in range(1,10):
    if i==5:
        exit()

    print(i)