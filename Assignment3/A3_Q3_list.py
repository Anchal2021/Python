def lstmin():
    lst=[]
    num=int(input("Enter a number:"))
    for i in range(1,num+1):
        ele=int(input("Enter a values:"))
        lst.append(ele)
    print("list of elements:",lst)
    m=min(lst)
    return m

def main():
    print("Minimum element from list:",lstmin())
if __name__=="__main__":
    main()
