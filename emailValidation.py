email = input("enter your email: ")
k, d = 0, 0
if len(email) > 8:
    if email[0].isalpha():
        if email[0].islower():
            if '@' in email and email.count('@') == 1 and email.count('.') == 1:
                if email[-3] == '.' or email[-4] == '.':
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isdigit():
                            continue
                        elif i == '_' or i == '.' or i == '@':
                            continue
                        else:
                            pass
                    if k == 1 or d == 1:
                        print('Wrong hai')
                    else:
                        print('Right email')

                else:
                    print('Wrong email 2')
            else:
                print('Wrong email format')
        else:
            print('First letter should be lower case')
    else:
        print('First letter should be an alphabet')
else:
    print('Length of the email should be 8')

# if '.' in email[-3] or '.' in email[-4]:
