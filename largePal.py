def main():
    print(palindrome())

def palindrome():
    for a in range(9,-1,-1):
        for b in range(9,-1,-1):
            for c in range(9,-1,-1):
                num = int(str(a)+str(b)+str(c)+str(c)+str(b)+str(a))
                print(num)
                for i in range(999,100,-1):
                    if (num%i==0) and (num/i <1000):
                        return num
    return 0
main()
