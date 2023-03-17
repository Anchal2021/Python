from Marvellousnum import chkprime

def lstprime():
    lst1=[]
    num=int(input("Enter a number="))
    for i in range(1,num+1):
        ele=int(input("Enter a Element="))
        lst1.append(ele)
    print("List is=",lst1)

    chkprime(lst1)



def main():
    lstprime()


if __name__=="__main__":
    main()
        

    
