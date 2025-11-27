def numberOfChild(n:int,k:int)->int:
    lst=list(i for i in range(0,n))+list(j for j in range(n-2,-1,-1))
    # print(lst)
    x=k%(2*(n-1))
    # print(x)
    return lst[x]
        
# print(numberOfChild(6,16))
"""
The ball returns to orignal position 0 after 2*(n-1) seconds
It means it does not matter how large or small k is 
The pattern will repeat itself after an interval of 2*(n-1) seconds
I created a lst=[0,1,2...n-2,n-1,n-2,n-3,...0]
So that it is easy to store the data
"""