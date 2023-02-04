age = 20
name = "dhanush"

#we cant concatenate int datatype to string 
#hence we do type casting here
print("my age is" + str(age) + " years")

#this can be replaced by .format 

print("my age is {0} years".format(age))
print("my age is {0} years and my name is {1}"
      .format(age,name))

#day in months of year

print("there are {0} days in {1},{2} months"
      .format(31,"jan","march"))

print("jan: {2},feb: {0},mar: {2}"
      .format(31,21,11))

print("""
      jan : {0}
      Feb : {1}
      mar : {2}
      apri: {3}
      may : {4}
      jun : {5}
      july: {6}""".format(10,20,30,40,50,60,70))

