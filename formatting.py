#printing squares and cubes using format method
for i in range(1,13):
    print("no.{0} squared is {1} and cubed is {2}" 
          .format(i,i**2,i**3))
for i in range(1,13):    
#to get allign in console we do     
    print("no.{0:>3} squared is {1:>4} and cubed is {2:>5}" 
          .format(i,i**2,i**3))
for i in range(1,13):    
    print("no. {0:2} squared is {1:<3} and cubed is {2:^4}" 
          .format(i,i**2,i**3))
    

print()

print("pi value is appproximately equal to {0:12}".format(22/7))
print("pi value is appproximately equal to {0:12f}".format(22/7)) #deciding no of values after the decimal point
print("pi value is appproximately equal to {0:<12.50f}".format(22/7))

#f_strings 

age_in_words = "24 years"
age = 24
#print("age of dhanush is" + age + "years ") this cant concatenate
print("age of dhanush is" + f" {age} years")

#printing pi value using f strings 
print(f"pi value is approximately equal to {22/7}")







