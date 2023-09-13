import sys

print("\nLearnSmasher Ceaser Cipher")
print("---------------------------------\n")

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
         'u','v','w','x','y','z']

def encryption(plain,shift):
    cipher = ""
    for char in plain:
        if char in alpha:
            pos = alpha.index(char)
            brapos = (pos+shift)%26
            cipher += alpha[brapos]
        else:
            cipher += char
    print(f"Encrypted Text : {cipher}\n")

def decryption(cipher,shift):
    plain = ""
    for char in cipher:
        if char in alpha:
            pos = alpha.index(char)
            brapos = (pos-shift)%26
            plain += alpha[brapos]
        else:
            plain += char
    print(f"Decrypted Text : {plain}\n")

finish = False
while not finish:
    print("Enter 1 for Encryption\nEnter 2 for Decryption\n")
    cryption = input("Enter Your Choice : ")
    message = input("Type your Message:  ").lower()
    shift_no = int(input("Type the Shift Number:   "))

    if cryption=="1":
        encryption(plain= message,shift=shift_no)

    elif cryption=="2":
        decryption(cipher=message,shift=shift_no)

    again = input("Enter 'YES' to play again, else 'QUIT' to quit:   ")
    print("\n")
    if again=="QUIT":
        finish=True
        print("\nThank You for using LearnSmasher Ceaser Cipher !!\n")
        sys.exit()