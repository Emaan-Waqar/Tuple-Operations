def multiplication(tup):
    product=1
    for i in tup:
        product = product*i  
    return product
tup1= (4,3,2,2,-1,18)
tup2= (2,4,8,8,3,2,9)
print("Product of tuple 1 is", multiplication(tup1))
print("Product of tuple 2 is", multiplication(tup2))

