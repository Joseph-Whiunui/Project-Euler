def main():
    num = 100
    sumSquares = sumOfSquares(num)
    squareSum = squareOfSums(num)
    answer = squareSum - sumSquares
    print(answer)

def sumOfSquares(num):
    answer = 0
    for i in range(num+1):
        answer += i**2
    return answer

def squareOfSums(num):
    answer = 0
    for i in range(num+1):
        answer += i
    return answer ** 2
        
    
main()
