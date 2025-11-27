from math import comb
def valueAfterKSeconds(n:int,k:int)->int:
    x=comb(n+k-1,k)
    return x

"""
Logic
Use pascal triangle for it
for n=2 values goes as 2C1,3C2,4C3...
for n=3 values goes as 3C1,4C2,5C3,6C4....
"""