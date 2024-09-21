a=[1,2,3,4,5]
b= 3
def change(a):
    global b
    b= -1
    a[2]=-1
print(b,a)
change(a)
print(b,a)
