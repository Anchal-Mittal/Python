def fun():
    
    import matplotlib.pyplot as plt
    x1=[1,2,4]
    y1=[2,5,15]
    tick_label=["a","b","c"]
    plt.bar(x1,y1,color=['red','blue'],tick_label=tick_label,width=0.5)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("bar graph")
    plt.legend()
    plt.show()

fun()    
    
