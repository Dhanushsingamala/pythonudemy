shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

for item in shopping_list:
    if item != "spam":   #to exclude only one item 
        print("buy " +  item)
   
#using break and continue to understand them better        

for item in shopping_list:
    if item == 'spam':
        continue            #just skips iteration of spam
    
    print("buy "+ item)        
   
#using break    

for item in shopping_list:
    if item == 'spam':
        break              #stops entire iterations from spam encountered
    
    print("buy "+ item)    
    

shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

item_to_find = "spam"
found_at = None

#for index in range(6)
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
        
print("item found at position : {0} mean index {1}".format(found_at + 1,found_at))
        


shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

item_to_find = "spammer"
found_at = None

#for index in range(6)
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is not None:       
    print("item found at position : {0} mean index {1}".format(found_at + 1,found_at))
else:
    print("{} is not found in shopping list".format(item_to_find))
    

#to decrease code 

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:       
    print("item found at position : {0} mean index {1}".format(found_at + 1,found_at))
else:
    print("{} is not found in shopping list".format(item_to_find))
    
    
        