# Import Module
import hashlib

print("\nLearnSmasher Hash Function Generator")
print("----------------------------------------\n")


print(f"""
         
   Select Your Choice from Below List 
   ------------------------------------
   01. For having MD5 type of Hashing
   02. For having sha1 type of Hashing
   03. For having sha224 type of Hashing
   04. For having sha256 type of Hashing
   05. For having sha384 type of Hashing
   06. For having sha3_224 type of Hashing
   07. For having sha3_256 type of Hashing
   08. For having sha3_384 type of Hashing
   09. For having sha3_512 type of Hashing
   10. For having sha512 type of Hashing
      
"""
)


getanumber = input(f"Enter your Choice : ")
password = input("Enter Your Text : ")


def update(hashvalue):
    hashvalue.update(password.encode("utf-8"))



def finalhash(hashvalue):
    output = f"Hashed Output  : {hashvalue.hexdigest()}"
    print(output)
    print("\n")


try:
    while True:
        if getanumber == "1" or "01":
            hash1 = hashlib.md5()
            update(hash1)
            finalhash(hash1)
            break
        if getanumber == "2" or "02":
            hash1 = hashlib.sha1()
            update(hash1)
            finalhash(hash1)
            break
        if getanumber == "3" or "03":
            hash1 = hashlib.sha224()
            update(hash1)
            finalhash(hash1)
            break
        if getanumber == "4" or "04":
            hash1 = hashlib.sha256()
            update(hash1)
            finalhash(hash1)
            break
        if getanumber == "5" or "05":
            hash1 = hashlib.sha384()
            update(hash1)
            finalhash(hash1)
            break
        if getanumber == "6" or "06":
            hash1 = hashlib.sha3_224()
            update(hash1)
            finalhash(hash1)
            break
        if getanumber == "7" or "07":
            hash1 = hashlib.sha3_256()
            update(hash1)
            finalhash(hash1)
            break
        if getanumber == "8" or "08":
            hash1 = hashlib.sha3_384()
            update(hash1)
            finalhash(hash1)
            break
        if getanumber == "9" or "09":
            hash1 = hashlib.sha3_512()
            update(hash1)
            finalhash(hash1)
            break
        if getanumber == "10":
            hash1 = hashlib.sha512()
            update(hash1)
            finalhash(hash1)
            break
        else:
            print("Please Enter a Number Between 1 or 10.")

except Exception as err:
    print(f"An Error Occured : {err}")