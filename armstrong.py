def armstrong(string):
    length=len(str(string))
    tempString =string
    result=0
    while tempString>0 :
        num=tempString % 10
        result+= num**length
        tempString //= 10
    if string == result:
        print("given number is armstrong ")
    else:
        print("the given string is not armstrong ")

def main():
    string=int(input("ENTER THE STRING "))
    armstrong(string)
   
        
if __name__=='__main__':
    main()
