parrot = "Nowegian Blue"
#[a:b:c] where a is starting index b is ending index and c is skibbale characters number
print(parrot[0:4:1]) 


number = "10,20,30,40,50,60,70,80,90,100"

print(number[1::3]) #not provide ending so it goes entires string starting from 1 slipping 3 characters 

#slicing bacckwards 
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] #it doesnt include first character
backwards1= letters[25::-1] #it include first character
print(backwards)
print(backwards1)

#to slice qpo,edcba,8char in rev,

qpo = letters[16:13:-1]
edcba = letters[4::-1]
last8 = letters[25:17:-1]

print(qpo) #CAN directly print as print(letters[index])
print(edcba)
print(last8)

#slicing idioms 
print(letters[-4:])
print(letters[-1:]) #last value will get printed 
print(letters[:1]) #only first value will get printed 
print(letters[0])

#if input string is empty then //index out of range // will pop out