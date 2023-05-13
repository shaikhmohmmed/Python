import deprecation
from math import pow
def Deprecation(v,r,t):
     Dep = v * pow ((1-r /100 ), t)
     return Dep
 

if __name__ == "__main__":
    V = float(input('Enter the intial values: '))
    R = float(input("Enter Rate: "))
    T = float(input("Enter the year: "))
    
    print(f"The Deprecation value is {int(Deprecation(V,R,T))}")     