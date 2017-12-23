def fun():
    set1=set()
    set2=set()
    for i in range(0,6):
        set1.add(i)
    print(set1)
    for i in range(4,10):
        set2.add(i)
    print(set2)
    print("union of set1 and set2" ,set1|set2)
    print("intersection of set1 and set2" ,set1&set2)
    if set1==set2 :
        print("both sets are equal")
    elif set1>set2:
        print("set1 is superset of set2")
    elif set1< set2:
        print("set1 is subset of set2")
fun();
    
