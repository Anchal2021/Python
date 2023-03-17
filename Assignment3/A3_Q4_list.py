def lstcnt():
    lst=[]
    num=int(input("Enter a number:"))
    for i in range(1,num+1):
        ele=int(input("Enter a value:"))
        lst.append(ele)
    print("List of elements :",lst)
    s=int(input("Enter a value to find count:"))
    count=lst.count(s)
    return count

def main():
    print("count of element is",lstcnt())
if __name__=="__main__":
    main()
        
