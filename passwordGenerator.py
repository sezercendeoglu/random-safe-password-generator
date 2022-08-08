import random
import array
from sre_parse import DIGITS
from symtable import Symbol
max=int(input("Enter max length?   ="))
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

upperAlpahabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

lowerAlpahabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

gatherPassword=numbers+upperAlpahabet+lowerAlpahabet+symbols

randomNumber=random.choice(numbers)
randomUpper=random.choice(upperAlpahabet)
randomLower=random.choice(lowerAlpahabet)
randomSymbol=random.choice(symbols)

temp_pass=randomLower+randomNumber+randomSymbol+randomUpper+randomSymbol

for x in range(max-4):
    temp_pass=temp_pass+random.choice(gatherPassword)
    temp_pass_list=array.array('u',temp_pass)
    random.shuffle(temp_pass_list)
    password = ""
for x in temp_pass_list:
        password = password + x
         
# print out password
print("Created your password:  "+password)