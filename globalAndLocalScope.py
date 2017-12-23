def ifelseFun():
    def fun():
        s="Hii this is Anchal Mittal"
        print(s)#local scope
    s ="Computer science department"#global scope
    print(s)
    fun()
    print(s)
ifelseFun();              
