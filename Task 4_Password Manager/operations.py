from makinghash import decode_password, encode_password, hash_master_password
import elara
from stdiomask import getpass

def new_password(db):
    
    website = input("Enter Application Name for the Password :- ")
    password = getpass(prompt = "Enter Password :- ", mask = '*')
    db.set(website, encode_password(password))
    print("\nPassword added Succesfully.")
    return db


def view_password(db):
    print("Applications for which Passwords have been Saved :-  ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j, ". ", i)
        j+=1
        
    index = int(input("\nEnter Application Number to Show Password :- "))
    if index>0 and index<=len(keys): 
        print("Password - ",decode_password(db.get(keys[index-1])))

    
def delete_password(db):
    print("Applications for which Passwords have been Saved :-  ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j, ". ", i)
        j+=1
    
    index = int(input("\nEnter Application Number to Delete Password :- "))
    verify_master_password_unhashed = getpass(prompt = "Enter Master Password for Authentication :- ", mask = '*')
    verify_master_password = hash_master_password(verify_master_password_unhashed)
    if verify_master_password == db.get("Masterpassword"):
        if index>0 and index<=len(keys):
            db.rem(keys[index-1])
            # Del website and password from dict
            print("\nPassword Deleted Succesfully.")
    else:
        print("Authentication Failed. Password not Deleted.")

    return db

def update_password(db):
    print("Applications for which Passwords have been Saved :- ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j, ". ", i)
        j+=1
    
    index = int(input("\nEnter Application Number to Update Password :- "))
    verify_master_password_unhashed = getpass(prompt = "Enter Master Password for Authentication - ", mask = '*')
    verify_master_password = hash_master_password(verify_master_password_unhashed)
    if verify_master_password == db.get("Masterpassword"):
        if index>0 and index<=len(keys):
            newpass = getpass(prompt = "Enter new password - ", mask = '*')
            db.set(keys[index-1], encode_password(newpass))
            print("\nPassword Updated Succesfully.")
            
        else:
            print("Authentication Failed. Password not Updated.")

    return db