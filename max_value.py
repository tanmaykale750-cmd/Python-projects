a=0
user=input("Enter a string: ")
list_u=user.split(" ")
list_u=list(map(int,list_u))
for i in list_u:
    if i>a:
        a=i
print("The largest number is:",a)



