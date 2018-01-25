import math

def main():
    num = 20
    primes = totalPrimes(num)
    numPerPrime = tallyPrimes(primes)
    print(numPerPrime)
    answer = productOfPrimes(numPerPrime)
    print(answer)
    

def productOfPrimes(totalPrimes):
    answer = 1
    for prime in totalPrimes:
        answer = answer * prime ** totalPrimes[prime]
    return answer

def tallyPrimes(primesOfRange):
    totalPrimes = dict()
    for primes in primesOfRange:
        curr = 1
        counter = 0
        for prime in primesOfRange[primes]:
            if (curr != prime):
                if counter!=0:
                    if curr in totalPrimes:
                        totalPrimes[curr] = max(totalPrimes[curr], counter)
                    else:
                        totalPrimes[curr] = counter
                curr = prime
                counter = 1
            else:
                counter += 1
        if curr in totalPrimes:
            totalPrimes[curr] = max(totalPrimes[curr], counter)
        else:
            totalPrimes[curr] = counter
    return totalPrimes

def totalPrimes(num):
    primes = dict()
    checked = dict()
    for i in range(1,num+1):
        currPrimes = findPrimes(i, checked)
        primes[i] = currPrimes
    return primes

def findPrimes(num, checked):
    if num <=1:
        return []
    if num in checked:
        return checked[num]
    root = math.sqrt(num)
    root = int(root)
    for i in range(2,root+1):
        if num%i==0:
            answer = [i] + findPrimes(num//i, checked)
            checked[num] = answer
            return answer
    checked[num] = [num]
    return [num]
        
                     

main()
