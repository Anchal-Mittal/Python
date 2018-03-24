def fun():
    array=[2,9,6,7,5]
    size=len(array)
    print(array)
    for i in range(0,size):
        for j in range(0,size):
            if(array[i]<array[j]):
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
    print(array)           
                
fun();      
