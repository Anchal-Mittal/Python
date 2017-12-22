import array
def arrayFun():
    arr1=array.array('I',[1,2,8,9,4,1,3])#creating unsigned array;**ERROR WHEN WE INSERT SIGNED VALUE
    for i in range(0,7):
      print(arr1[i],end=" ")#for space we r using end
    print(arr1.typecode)#find the type of the element in the array
    print(arr1.itemsize)#give the size of single element in byte
    print(arr1.buffer_info())#Returns a tuple representing the address in which array is stored and number of elements in it.
    print(arr1.buffer_info)#only give the addess in which array is stored

arrayFun();

      
      
      
    
