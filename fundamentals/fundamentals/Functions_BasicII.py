def Countdown():
    for i in range (5,0, -1):
        print(i)
Countdown()

def Print_Return():
    x=[]
    for i in (0,1):
        print(x[0])
        return x[1]
Print_Return([1,2])
