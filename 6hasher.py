import hashlib  #it performs hashing itself with few lines o code

hashvalue = input("Enter a string to hash: ")

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode()) 
#this will add  a string o hash object which we'll turn into md5 hash with hexdigest functn
print(hashobj1.hexdigest())


hashobj2 = hashlib.sha1()
#this is sha1 hash
hashobj2.update(hashvalue.encode())
print(hashobj2.hexdigest())

hashobj3 = hashlib.sha224()
#this is sha224 hash
hashobj3.update(hashvalue.encode())
print(hashobj3.hexdigest())

hashobj4 = hashlib.sha256()
#this is sha256 hash
hashobj4.update(hashvalue.encode())
print(hashobj4.hexdigest())

hashobj5 = hashlib.sha512()
#this is sha512 hash
hashobj5.update(hashvalue.encode())
print(hashobj5.hexdigest())