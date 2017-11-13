import random

def d():
       print(random.randrange(100,1000,2))
       print(random.randrange(100,1000,3))
       print(random.choice([1,2,3,5,6]))
       print(random.random())#produce a random number r such that 0<r<1
       random.seed(100)
       print(random.random())
       list =[1,3,9,6,4]
       x=5
       y=10
       random.shuffle(list)
       print(list)#reshuffled the list
       print(random.uniform(x,y))# generate random number r such that x<=r<=y
       
d();
    

    
