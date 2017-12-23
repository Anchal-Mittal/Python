def fun():
    str="hye i m just try to learn python"
    str1="aeiouAEIOU"
    vowel=set(str1)
    count=0
    for alphabet in str:
        if alphabet in vowel:
            count=count+1
    print("PRINT THE TOTAL NUMBER OF VOWELS",count)        
fun();
    
