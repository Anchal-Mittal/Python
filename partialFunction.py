from functools import *
def partialFun():
    def add(a,b,c):
       return a*100+10*b+c
        
    add_fun=partial(add,2,3)#assigning a=2,b=3
    print(add_fun(3))#assigning c=3 
partialFun();    
 """Partial functions allow us to fix a certain number of arguments of a function and generate a new function."""
   
    
