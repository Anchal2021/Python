def star():

    num=int(input("Enter a number="))
    for num in range(1,num+1):
        print("*" ,end=" ")

def main():
    star()

if __name__=="__main__":
    main()
