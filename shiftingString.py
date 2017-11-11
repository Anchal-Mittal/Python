def fun():
    print("CONVERSION INT TO CHAR AND VICE - VERSA ")
    # ord() function will convert char to int
    print(ord('A'))
    # chr() function will convert int to char
    print(chr(98))
    print("SHIFTING A CHARACTER BY 2")
    print(chr(ord('k')+2))
    print("SHIFTING z CHARACTER DOES NOT RETURN ANOTHER CHARACTER")
    print(chr(ord('z')+2))#return |
    print("CREATING CIRCULAR SHIFT")
    print(chr((((ord('z')+2)-ord('a'))%26)+ord('a')))

    print("TRANSLATING THE WHOLE STRING ")
    result= " "
    raw ="g fmnc 123s bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(raw)
    for c in raw:
      if c < 'a' and c > 'z':
         result +=chr((((ord('z')+2)-ord('a'))%26)+ord('a'))
      else :
         result += c

    print(result)
    
fun();
    
