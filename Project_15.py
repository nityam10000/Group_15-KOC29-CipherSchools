num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
count_prime = count_composite = 0
for num in range(num1,num2+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                count_composite += 1
                print(num,"is a COMPOSITE number")
                break
        else:
            count_prime += 1
            print(num,"is a prime number")    
    elif num == 0 or 1 :
        print(num,"is neither a PRIME nor a COMPOSITE number")
    else:
        print()
print(count_prime, "prime and", count_composite , "composite numbers in range")