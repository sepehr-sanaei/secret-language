def encode():
    message = input("Enter your message: ")
    ls = []
    for i in message:
        new_ord = ord(i) + 4
        ls.append(chr(new_ord))

    print(''.join(ls))

def decode():
    message = input("Enter your message: ")
    ls = []
    for i in message:
        old_ord = ord(i) - 4
        ls.append(chr(old_ord))
    print(''.join(ls))
a = True
while a:    
    choice = int(input("Do you want to Encode(1) or decode(2) or exit(0): "))
    if choice == 1:
        encode()
    elif choice == 2:
        decode()
    elif choice == 0:
        a = False
    else:
        print("Wrong choice!!")