"""
A Tuple is a collection of Python objects separated by commas.
In someways a tuple is similar to a list in terms of indexing,
nested objects and repetition but a tuple is immutable unlike lists
which are mutable.

"""
def fun():
    print("Empty tuple")
    empty_tuple=()
    print(empty_tuple)
    tuple1=(0,9,8,7)
    tuple2=("hello","world","\n")
    tuple3=tuple1+tuple2
    print(tuple3,"\n")
    tuple3=(tuple1,tuple2)
    print(tuple3)
    print(tuple1[1:])
    print(tuple1[::-1])
    print(tuple1[2:4])
    print("length of the tuple1 =",len(tuple1))
fun()    
    
    
    
