#Write a program to perform the following operations: 
# 1. Create a tuple with different datatypes 
# 2. Create another tuple of integers 
# 3. Create a new tuple by adding 9 to the previous tuple 
# 4. Count the occurrences of an element in the tuple 
# 5. Perform slicing on the tuple

a=(1,3.5,"Emaan",True)
b=(1,3,7,8,9)
#b[5]= 9 (We cannot change an element in a tuple)
element= int(input("Enter the value you want to check: "))
for i in b:
    if element == i:
        print("element found",i)

print(a[1:3])





