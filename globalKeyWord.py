def Fun():
      s=9
      def globalFun():
            global s# here global is used to modify the global value
            s=78
            print(s)
            s="ANCHAL MITTAL:"
            print(s)
        
      s ="Computer science department"#global scope
      print(s)
      globalFun()
      print(s)
    
      """def localFun ():
           print(s)# here s is a local variable which is referencing before assingment
           s="ANCHAL MITTAL IS FINE:"
           print(s)"""
      print(s)  
      s ="Computer science department is nice one"#global scope
      print(s)
      #localFun()
      print(s)
Fun();              
v
