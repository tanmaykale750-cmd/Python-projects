import random
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):

    password=[]
    chars=""
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower='abcdefghijklmnopqrstuvwxyz'
    digits='0123456789'
    special='!@#&*'
   

    if use_upper:
        chars+=upper
    if use_digits:
        chars+=digits
    if use_special:
       chars+=special
    if use_lower:
        chars+=lower
    if chars=="":
        print("User needs to select atleast one category")
        return None
    elif length<4:
        print("There should atleast be 4 charecters")
        return None

    else:
        for i in range(length):
            password.append(random.choice(chars))
    random.shuffle(password)
    return "".join(password)
print(generate_password(length=10, use_special=False))

            
