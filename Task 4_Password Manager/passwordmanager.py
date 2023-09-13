from stdiomask import getpass
import json
import elara
import hashlib

from makinghash import decode_password, encode_password, hash_master_password
from operations import new_password, view_password, delete_password, update_password


def set_master_password():
    print("\nLearnSmasher Password Manager ")
    print("-----------------------------------------")
    master_password = getpass(prompt = "Set Master Password for Application :- ", mask = '*')
    return hash_master_password(master_password)



def intialise_db():
    db = elara.exe_secure("data.db", True)
    
    if not db.exists("Masterpassword"):
        db.set("Masterpassword", set_master_password())
    return db



def main():
    db = intialise_db()
    verify_master_password_unhashed = getpass(prompt = "Enter the Master Password :-  ", mask = '*' )
    verify_master_password = hash_master_password(verify_master_password_unhashed)
    if verify_master_password == db.get("Masterpassword"): 
        print("\nSelect your Choice from the Below List ")
        print("------------------------------------------\n")
        while(1):
            print(" ")
            print("1. Add a New Password")
            print("2. Show a Password")
            print("3. Delete a Password") 
            print("4. Update a Password") 
            print("5. Quit ")
            print(" ")

            choice = int(input("Enter Your Choice :- "))
            if choice == 1:
                db = new_password(db)
            elif choice == 2:
                view_password(db)
            elif choice == 3:
                db = delete_password(db)
            elif choice == 4:
                db = update_password(db)
            elif choice == 5:
                print(" ")
                print("Thank you !! Visit again !! \n")
                break
            else:
                print("Invalid choice.")

            
    else:
        print("Authentication Failed.")

main()