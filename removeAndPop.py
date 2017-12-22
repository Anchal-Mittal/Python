import array
def arrayFun():
    arr=array.array('I',[1,2,8,9,4,3])#creating unsigned array;**ERROR WHEN WE INSERT SIGNED VALUE
    for i in range(0,6):
      print(arr[i],end=" ")#for space we r using end
    print("\r") #print in next line
    print("after pop element at location 2")  
    arr.pop(2)#pop the 2 position element
    for i in range(0,5):
      print(arr[i],end=" ")#for space we r using end
    print("\n") #print after droping one line
    arr1=array.array('i',[1,-2,3,5,8,9,6,5])#creating signed array;**NOT ERROR DUE TO -2
    for i in range(0,8):
      print(arr1[i],end=" ")
    print("\n")    
    print("after removing 5 in arr1");  
    arr1.remove(5)#remove first occurrence of 5
    for i in range(0,7):
      print(arr1[i],end=" ")
    #arr1.remove(10) ***Error bcz element 10 is not exist 
   
arrayFun();

      
      
      
    
