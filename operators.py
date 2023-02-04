a=12
b=15

print(a//b) #rounds of the float value to integer
print(a/b)
print(a+b)
print(a*b)
print(a-b) 
print(a%b) #modulo operator returns remainder

c=15
d=5

for i in range(1,c//d):
    print(i)
    

# operator precedence 
print(a+b /3-4*12)
print(a+(b/3)-(4*12))
print(((a+b)-c)+d*4) #based on precedence of the operator displays results


