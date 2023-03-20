from functools import reduce

lst=[]
num=int(input("Enter a digit:"))
for i in range(1,num+1):
    ele=int(input("Enter a values:"))
    lst.append(ele)
print("list is:",lst)


Even_list=list(filter(lambda ele:(ele%2==0),lst))
print("Even numbers from list are:",Even_list)

Sq_list=list(map(lambda ele:ele**2,Even_list))
print("square of numbers from list:",Sq_list)

Add_list=reduce(lambda a,b:(a+b),Sq_list)
print("Addition of list is:",Add_list)
