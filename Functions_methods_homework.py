#FInding volume of sphere
from audioop import mul
from curses.ascii import islower, isupper
from hmac import new
from itertools import count
from operator import le
import re
import string



def vol(rad):
    return ((4/3)*3.1416*(rad**3))

#Finding the function is in the function or not 
def Range_checker(num1,start,end):
    if(num1>start and num1<end):
        print(f'{num1} is in the range {start} and {end}')

    else:
        print(f'{num1} is not in the given range')

#finding number of upper and lowercase letter in the given string 
def Finder(fun_string):
    upper_count=0
    lower_count=0
    for x in fun_string:
        if isupper(x):
            upper_count+=1
        elif islower(x):
            lower_count+=1
        
    print(f'Numebr of Uppercase in the give string are:{upper_count}\nNumber of lowercase letters:{lower_count}')


#unique list
def uniquer(fun_list):
    new_list=[]
    length=0
    new_list.append(fun_list[0])
    for x in fun_list:
        if new_list[length]!=x:
            new_list.append(x)
            length+=1
            
    print("\nGive list",fun_list)
    print(f'\nUnique list:{new_list}')


#List element multipler
def Element_multipler(Multiplying_list):
    container=1
    for x in Multiplying_list:
        container*=x
    print(container)


#Palindrome_checker
def Palindrome_checker(value):
    length=len(value)
    length-=1
    counter=0
    for x in value:
        if(value[length]==x):
            print(x,value[length])
            counter+=1
        if(counter==(len(value)-1)/2):
                break
        length-=1

    if(counter==((len(value)-1)/2)):
        print("The given string is palindrome")
    else:
        print("The given string is not palindrome")


#Pangram function 
def Pangram_function(value,alphabet=[string.ascii_lowercase]):
    letter_counter=0
    value=value.lower()
    value=set(value)
    result=''.join(value)
    result=result.replace(' ','')
    for i in result:
        for x in string.ascii_lowercase:
            if(i==x):
                letter_counter+=1
    if(letter_counter==26):
        print("The given string contain all the alphabets")
        print(letter_counter)
    else:
        print(letter_counter)
        print("THe given string don't contain all the alphabets")


            




#main Function
print("Enter the value of Radius:")
radius=int(input())
print(vol(radius))
Range_checker(15,0,20)


print("\nEnter the string to find how many upper and lower case letter are in it")
mystring=input()
Finder(mystring)

mix_list=[1,1,1,1,2,3,3,3,4,4,4,5,5,5,6,6]
uniquer(mix_list)

print('Multiplying Element of the given list')
mul_list=[1,2,3,4,5]
Element_multipler(mul_list)

print("\nEnter any word to check it is palindrome or not:")
myvalue=input()
print(Palindrome_checker(myvalue))

print("\nPangram function calling ")
Pangram_function("The quick brown fox jumps over the lazy dog")