#user define function
import enum
from hmac import new
import string


def Macdonal_func(name):
    new_name=""
    for i,char in enumerate(name):
        if(i==3 or i==0):
            new_name=new_name+(char.upper())
        else:
            new_name+=char
    return new_name


#Main function
print(Macdonal_func('myname'))