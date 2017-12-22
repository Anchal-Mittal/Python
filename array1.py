import array
def arrayFun():
    arr=array.array('I',[1,2,3])#creating unsigned array;**ERROR WHEN WE INSERT SIGNED VALUE
    for i in range(0,3):
      print(arr[i],end=" ")#for space we r using end
    arr1=array.array('i',[1,-2,3])#creating signed array;**NOT ERROR DUE TO -2
    for i in range(0,3):
      print(arr1[i],end=" ")
arrayFun();

      
      
      
    
