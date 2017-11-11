import string

def strrr():
    
   raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

   a = "abcdefghijklmnopqrstuvwxyz,. '()"
   b = "cdefghijklmnopqrstuvwxyzab,. '()"

   print("".join([dict(zip(a,b))[x] for x in raw]))
   
   print(list(zip(a,b)))
   print(dict(zip(a,b)))
   
strrr();   
   
