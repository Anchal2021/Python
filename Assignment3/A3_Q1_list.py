def lstsum():
    lst=[]
    sum=0
    num=int(input("Enter a Digit="))
    for i in range(1,num+1):
        ele=int(input("Enter a value="))
        lst.append(ele)
    print("List is=",lst)
    sum=sum+ele
    return sum

def main():
    print("Sum of values in list is=",lstsum())
if __name__=="__main__":
    main()

    
