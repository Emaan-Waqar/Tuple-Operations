a=(1,2,3,3,2,1)
b= list(a)
b.reverse()
print(b)
c= tuple(b)
print(c)
if a==c:
    print("It is a palindrome.")
else:
    print("It is not a palindrome")    