# i=0
# sum=0
# while 1:
#     n=input("Enter a number :")
#     if n=="done" :
#         break
#     try :
#         m=int(n)
#         sum+=m
#         i+=1
#     except :
#         print("Enter an other number")
# print(sum,i,sum/i)
i=0
sum=0
while 1:
    n=input("Enter a number :")
    if n=="done" :
        break
    m=int(n)
    sum+=m
    i+=1
print(sum,i,sum/i)