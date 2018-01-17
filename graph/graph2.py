def fun():
    
    import matplotlib.pyplot as plt
    x1=[1,2,4]
    y1=[2,5,8]
    plt.plot(x1,y1, label="line1")
    x2=[7,3,8]
    y2=[6,8,13]
    plt.plot(x2,y2,label="line2")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("initial graph")
    plt.legend()
    plt.show()

fun()    
    
