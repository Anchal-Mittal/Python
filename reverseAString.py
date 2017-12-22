def reverse():
    var ="hello this side is anchal mittal"
    size=len(var)
    print(size)
    reverseVar=var[size-1]
    i=size-1
    while (i>0):
       i=i-1
       reverseVar=reverseVar+var[i]
    print(reverseVar)
reverse();
    
