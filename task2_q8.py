s = input ("input a string:-")
num=0
char =0

for x in s:
    if x.isdigit():
        num=num+1
    elif x.isalpha():
        char=char+1
print("Total digits are",num)
print("Total character are",char)
