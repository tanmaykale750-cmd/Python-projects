
user_input=input("Enter numbers: ")
numbers=user_input.split(" ")
numbers=list(map(int,numbers))
max_value=numbers[0]
for i in numbers:
    if i>max_value:
        max_value=i
print("The largest number is:",max_value)






