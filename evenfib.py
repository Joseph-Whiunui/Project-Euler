def main():
    total = fib()
    print(total)
    

def fib():
    first = 1
    second = 2
    total = 0
    while second <=4000000:
        if second%2==0:
            total += second
        temp = first + second
        first = second
        second = temp
    return total


    
main()
