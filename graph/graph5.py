def fun():
    
    import matplotlib.pyplot as plt
    x1=[1,5,8,13,19,45,35,30]
    range=(0,50)
    bins=5
    tick_label=["a","b","c"]
    plt.hist(x1,bins,range,color='red',histtype='bar',rwidth=0.5)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("hist graph")
    plt.legend()
    plt.show()

fun()    
    
