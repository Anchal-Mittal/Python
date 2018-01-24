"""
A Tuple is a collection of Python objects separated by commas.
In someways a tuple is similar to a list in terms of indexing,
nested objects and repetition but a tuple is immutable unlike lists
which are mutable.

"""
import numpy
def fun():
    tuple1=(1,2,3,4,5,6)
    tuple2=(4,3,4,2,1,2)
    for i in range(0,5) :
        tuple1=(tuple1,)
        print(tuple1)
       
fun()    
    
    
    
