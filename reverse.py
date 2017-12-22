import array
def arrayFun():
    arr=array.array('I',[1,2,8,9,4,3])#creating unsigned array;**ERROR WHEN WE INSERT SIGNED VALUE
    for i in range(0,6):
      print(arr[i],end=" ")#for space we r using end
    print("\r") #print in next line
    print("after reverse element at location 2")  
    arr.reverse()#reverse the array's  element
    for i in range(0,6):
      print(arr[i],end=" ")#for space we r using end
arrayFun();

      
      
      
    
