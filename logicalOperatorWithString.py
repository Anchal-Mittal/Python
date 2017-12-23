def fun():
    str1=""
    str2="gud mrng"
    # repr is used to print the string alog with the quotes
    print(repr(str1 and str2))
    print(repr(str2 and str1))
    print(repr(str1 or str2))
    print(repr(str2 or str1))

fun();    
"""
The output of the boolean operations between the strings depends on following things:

1.Python considers empty strings as having boolean value of ‘false’ and non-empty string as having boolean value
of ‘true’.

2.For ‘and’ operator if left value is true, then right value is checked and returned. If left value is false, then it 
is returned

3.For ‘or’ operator if left value is true, then it is returned, otherwise if left value is false, then right value 
is returned."""
