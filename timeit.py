import timeit
 
# code snippet to be executed only once
mysetup = "from math import sqrt"
 
# code snippet whose execution time is to be measured
mycode = '''
def example_code():
    mylist = []
    for x in range(1000):
        mylist.append(sqrt(x))
'''
 
# timeit statement
print(timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 10000))
