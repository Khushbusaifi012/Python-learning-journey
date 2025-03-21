# 1.WAP TO FIND THE LENGTH OF A GIVEN STRING WITHOUT USING THE LEN FUNCTION?
# s=input("Enter a string  : ")
# output=0
# for i in s:
#     output+=1
# print("Length of a string is : ",output)

# 2.WAP TO EXTRACT USERNAME FROM A GIVEM EMAIL EX IF THE EMAIL IS KHUSHBUSAIFI278@GMAIL.COM THEN THE USERNAME SHOULD BE KHUSHBUSAIFI278?
# s=input('Enter a email : ')
# output=s.index('@')
# print(s[0:output])

# 3.WAP TO COUNT THE FREQUENCY OF A PARTICULAR CHARACTER IN A GIVEN STRING?
# s=input("Enter a string : ")
# term=input("What should like to search for : ")
# counter=0
# for i in s:
#     if(i==term):
#         counter+=1
# print('frequency is : ',counter)

# 4.WAP WHICH CAN REMOVE A PARTICULAR CHARACTER FROM A STRING?
# s=input("Enter a string  : ")
# term=input("what would like to remove : ")

# result=''
# for i in s:
#     if(i!=term):
#         result =result+i
# print(result)

# 5.WRITE A PROGRAM THAT CAN CHECK WHETHER A GIVEN STRING IS PALINDROME OR NOT?
# s=input("Enter a string  : ")
# flag=True
# for i in range(0,len(s)//2):
#     if(s[i]!=s[len(s)-i-1]):
#         flag=False
#         print("Not a palindrome numbers ")
#         break

# if(flag):
#         print("Palindrome numbers")

# 6.WRITE A PROGRAM TO COUNT THE NUMBERS OF WORDS IN STRING WITHPUT SPLIT()?
# s=input("Enter a string : ")
# l=[]
# temp=" " 
# for i in s:
#     if(i!=" "):
#         temp=temp+i
#     else:
#         l.append(temp)
#         temp=" "
# l.append(temp)
# print(l)

# 7.WRITE A PYTHON PROGRAM TO CONVERT A STRING TO TITLE CASE WITHOUT USING THE TITLE?
# s=input("Enter a string : ")
# l=[]
# for i in s.split():
#     l.append(i[0].upper()+i[1:].lower())
# print(" ".join(l))

# 8.WRITE A PROGRAM THAT CAN CONVERT AN INTEGER INTO AN STRING?
# num=int(input("Enter a string  : "))
# digits='0123456789'
# result=" "
# while(num!=0):
#     result=digits[num%10]+result
#     num=num//10
# print(result)
# print(type(result))