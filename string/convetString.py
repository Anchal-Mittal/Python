def convert(string):
    length=len(string)
    if length <3:
        return string
    tempString=string[length-3:length]
    if tempString=="ing":
        return tempString+"ly"
    else:
        return tempString+"ing"
def main():
    string=input("ENTER A STRING ")
    convertedString=convert(string)
    print("AFTER CONVERSION",convertedString)

if __name__== '__main__':
    main()
    
   
    
    
