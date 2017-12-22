import array
def arrayFun():
    arr=array.array('I',[1,2,3])#creating unsigned array;**ERROR WHEN WE INSERT SIGNED VALUE
    for i in range(0,3):
      print(arr[i],end=" ")#for space we r using end
    print("\r") #print in next line
    print("after insrt 4 at location 2")  
    arr.insert(2,4)
    for i in range(0,4):
      print(arr[i],end=" ")#for space we r using end
    print("\n") #print after droping one line
    arr1=array.array('i',[1,-2,3])#creating signed array;**NOT ERROR DUE TO -2
    for i in range(0,3):
      print(arr1[i],end=" ")
    print("\n")    
    print("after appending 5 in arr1");  
    arr.append(5)
    for i in range(0,3):
      print(arr1[i],end=" ")
   
arrayFun();

      
      
      
    
