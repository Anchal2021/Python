def lstmax():

    lst=[]
    num=int(input("Enter a Digit="))
    for i in range(1,num+1):
        ele=int(input("Enter a values="))    
        lst.append(ele)
    print("list is=",lst)
    m=max(lst)
    return m

def main():
   print("Maximum element from list is=",lstmax())
   

if __name__=="__main__":
    main()

