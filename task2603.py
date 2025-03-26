#Take a paragraph check the count of words, if count is more than 100, print valid ; else invald.
para=input("enter the paragraph") #take in put from user
new=para.split(" ")
for i in range (len(new)):
    print(i,new[i])
if len(new)>=100:
    print("valid")
else:
    print("invalid")


#Take  a input from with both upper and lower cases charcters count the no of uppercases and lowercases.
word=(input("enter the string contains both upper and lower case:"))
ucount=0
lcount=0
for i in range(len(word)):
        if ord(word[i])>=61 and ord(word[i])<=90:
            ucount+=1
        else:
            lcount+=1
print("there is",ucount,"upper case letters in the string")
print("there is",lcount,"upper case letters in the string")