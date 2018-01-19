def fun():
    
    import matplotlib.pyplot as plt
    x1=[1,5,8,13,19,45,35,30]
    y1=[2,5,3,3,2,4,4,6]
    plt.scatter(x1,y1,label="stars",color='red',marker="*")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("scatter diagram")
    plt.legend()
    plt.show()

fun()    
    
