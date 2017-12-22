def reverse():
    var ="Shello this side is anchal mittal"
    size=len(var)
    print(size)
    reverseVar=var[size-1]
    i=size-1
    for j in range(0,i):
        j=i-j
        reverseVar=reverseVar+var[j]
    reverseVar=reverseVar+var[0]
    print(reverseVar)
reverse();
    
