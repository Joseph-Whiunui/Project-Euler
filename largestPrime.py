def main2():
    product = 600851475143
    print(factor2(product))

def factor2(product):
    i = 2
    while i*i <= product:
        if product%i==0:
            return factor2(product//i)
        i+=1
    return product

main2()
