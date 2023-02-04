#         0123456789....  
parrot = "green in colour"

print(parrot)
print(parrot[3]) #returns value at 4th place index starts from 0 in py
print()
word = "Norwegian Blue"

#target is to print WE WIN line by line using word individually
#using positive indexing

print(word[3])
print(word[4])
print(word[9])
print(word[3])
print(word[6])
print(word[8])

print()

#using negative indexing last character is -1 and 
#this can done by subtracting stringlength from positive indexes(3-14=-11)

print(word[-11])
print(word[-1])
print(word[-5])
print(word[-11])
print(word[-8])
print(word[-6])

#slicing in strings using indexes
#[a:b] where a is starting index and b is ending index actually

description = "have a good day career ahead dhanush"

print(description[3:5])
print(description[0:6]) #starts at 0 and ends at 6
print(description[0:])  #prints till last
print(description[:-1]+description[-1]) #prints till last

#slicing a word career from description
#note ending index should be +1 to your ending character index in python
print(description[16:22])

print(description[:]) #prints complete string

#slicing using negative indexes 

define = "u r a good coder "

print(define[-1:0])



