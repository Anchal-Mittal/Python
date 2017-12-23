def fun():
    set1={1,2,3}
    set1.add(7)
    print(set1)
    set2={9,8,7,3}
    print(set1.union(set2))
    print(set1.intersection(set2))
    print(set1.difference(set2))
    print("clear",set2.clear)
fun();
    
