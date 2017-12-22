import array
def arrayFun():
    arr1=array.array('I',[1,2,8,9,4,1,3])#creating unsigned array;**ERROR WHEN WE INSERT SIGNED VALUE
    for i in range(0,7):
      print(arr1[i],end=" ")#for space we r using end
      
    print("\r") #print in next line
    
    print(arr1.count(1))#count the number of 1 in the array
    
    print("\r")
    
    arr2=array.array('I',[1,2,3,4,5])    
    
    print("extend arr1 to arr2")  
    arr1.extend(arr2)#reverse the array's  element
    for i in range(0,12):
      print(arr1[i],end=" ")#for space we r using end
    
    """arr3=array.array('i',[1,2,3,4,5])    
    print("extend arr1 to arr2")  
    arr1.extend(arr3)#reverse the array's  element
    for i in range(0,12):
      print(arr1[i],end=" ")#for space we r using end
     """#because we can extend the array of same kind  
arrayFun();

      
      
      
    
