from tkinter  import *
def main():
    m=Tk()
    m.title("WELCOME")
    button1=Button(m,text ='BUTTON1',width=25,fg="red",bg="yellow")
    button1.pack(side=LEFT)
    button2=Button(m,text ='BUTTON2',width=25,fg="red",bg="cyan")
    button2.pack(side=LEFT)
    button3=Button(m,text ='BUTTON3',width=25,fg="red",bg="green")
    button3.pack(side=RIGHT)
    button4=Button(m,text ='BUTTON4',width=25,fg="black",bg="yellow")
    button4.pack(side=BOTTOM)
   
    m.mainloop()
if __name__=='__main__':
    main()
    i
