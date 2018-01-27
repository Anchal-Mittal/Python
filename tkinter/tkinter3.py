from tkinter  import *
def main():
    m=Tk()
    m.title("WELCOME")
    button=Button(m,text ='NAME',width=25)
    button.pack()
    label=Label(m,text="hello",bg = "cyan",fg = "Red")
    label.pack()
    label=Label(m,text="gud mrng",bg = "cyan",fg = "Red")
    label.pack(fill =X)
    label=Label(m,text="gud evening",bg = "yellow",fg = "black")
    label.pack(fill=Y)
    m.mainloop()
if __name__=='__main__':
    main()
    
