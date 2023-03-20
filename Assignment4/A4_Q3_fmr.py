from functools import reduce

lst=[]
x=int(input("Enter digit:"))
for i in range(1,x+1):
    ele=int(input("Enter a value:"))
    lst.append(ele)
print("list is:",lst)

filter_list=list(filter(lambda ele:(ele>=70 and ele<=90),lst))
print("Filtered list is",filter_list)

map_list=list(map(lambda ele:(ele+10),filter_list))
print("List after Addition by ten:",map_list)

reduce_no=reduce(lambda a,b:(a*b),map_list)
print("reduced output:",reduce_no)
