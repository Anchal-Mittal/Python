def fun():
    
    import matplotlib.pyplot as plt
    x1=[1,2,4]
    y1=[2,5,8]
    plt.plot(x1,y1,color="RED",linestyle= "dotted",linewidth=3,marker='o',markerfacecolor="BLACK",label="line1")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("initial graph")
    plt.legend()
    plt.show()

fun()    
    
