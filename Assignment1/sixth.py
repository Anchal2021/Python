def chknum():
    num=int(input("Enter a number:"))
    if num<0:
        print("Number is negative")
    elif num>0:
        print("Number is positive")
    else:
     print("Number is Zero")
def main():
    chknum()
if __name__=="__main__":
    main()