#check if the list is which type 
vijay=["a","b","c","d"]
print(type(vijay))
#how to access the list items
santhi=["l","k","n","h"]
print(santhi[2])
#using range function
print(santho[1:2])
print(santhi[:3])
print(santhi[0:])
print(santhi[-4:-1])
#in negative indexing backword is not possible
#print empty list
print(santhi[-1:-4])
#add two lists using extend()

anil=["v","e","m","a","a","n","i","l"]
lakshmi=["l","a","k","s","h","m","i"]
print(anil)
print(lakshmi)
#change item values
anil.insert(2,"g")
print(anil)
#add two lists
anil.extend(lakshmi)
print(anil)
#adding two different tuple,list,set,dict
anil=["v","e","m","a","a","n","i","l"]
lakshmi=("l","a","k","s","h","m","i")
anil.extend(lakshmi)
print(anil)
#chage range of lists
anil=["v","e","m","a","a","n","i","l"]
anil[2:4]=["l","m"]
print(anil)
# one value to replace two values
anil=["v","e","m"]
anil[1:4]=["l","m"]
print(anil)
#append
anil=["v","e","m","a","a","n","i","l"]
anil.append("siva")
print(anil)
#remove
anil=["v","e","m","a","a","n","i","l"]
anil.remove('n')
print(anil)
#pop
anil=["v","e","m","a","a","n","i","l"]
anil.pop()
print(anil)
anil.pop(3)
print(anil)
#del
anil=["v","e","m","a","a","n","i","l"]
del anil[6]
print(anil)
#clear
anil=["v","e","m","a","a","n","i","l"]
anil.clear()
print(anil)






