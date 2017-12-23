def fun():
    str="hye i m just try to learn python"
    print(str.split())
    print(str.split(" ",1))#split the string into two parts on the bases of space
    print(str.split(" ",5))
fun();
"""
  output
['hye', 'i', 'm', 'just', 'try', 'to', 'learn', 'python']
['hye', 'i m just try to learn python']
['hye', 'i', 'm', 'just', 'try', 'to learn python']

REASONS
regexp is the delimiting regular expression; 
limit is limit the number of splits to be made 
str.split(regexp = "", limit = string.count(str)) 
"""
