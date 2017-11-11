def loop():
    # FINDING 2 ^ 38
    print("FINDING THE 2 ^ 38") 
    k = 1

    # USING LOOP
    print("using loop")
    for i in range(38) :
      k *= 2
    print(k)
          
    # USING POWER FUNCTION
    print("power function")
    result = pow(2,38)
    print(result)
          
    # USING POWER OPERATOR
    print("using power operator")
    result = 2 ** 38
    print(result)
          
    # USING LEFT SHIFT
    print("using shift operatot") 
    result = 1 << 38
    print(result)

loop();
    
