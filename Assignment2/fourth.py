
# sum of factors

def factsum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i

    return sum


def main():
    num = int(input("Enter a number:"))
    print(factsum(num))


if  __name__=="__main__":
    main()