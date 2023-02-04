for j in range (1,13):
         print("No .{} squared is {} and cubes is {:4}".format(j,j**2,j**3))

#create another block  out if this block to know indentation
print("*"*70)

name = input("please enter ur name:  ")
age = int(input("how old are you,{0}?".format(name)))
print("your age is %d" % age)

if age >=18:
    print("you are old enough to vote")
    print("please put an X in the box where u like to vote")
elif age<18:
    print("please come back after {0} years Mr/Ms.{1}".format(18-age,name))  
else:
    print("sorry request cant be processed we r checking on it please")  
    
#usually we make use of elif when we have more than 2 that is 3  conditions 


if age< 18:
    print("please come back after {0} years Mr/Ms.{1}".format(18-age,name))  
elif age > 70:
    print("i think u r dead! rest in peace my friend *")
else:
    print("you are eligible to vote please put an X in any of options listed here ")
    
 


 
    
   



    
