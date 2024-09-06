arr =[1,2,3,4]
b=9
ans =""
def changArr():
    brr=[1,3,4,5]
    b =1
    def changeBrr(b):
        b=2
        brr[2] = -1
    changeBrr(b)
    print("brr" ,brr,b)

    arr[2]=-1



print(arr,b,ans)
changArr()
print(arr,b,ans)
