#Write a Python program to identify prime numbers from the first 20 odd numbers.
odd= []
for i in range(0, 100):
    if i%2 != 0:
        odd.append(i)
    if len(odd) == 20:
        break

print("First 20 odd numbers:", odd)

# find prime numbers from this list
primes = []

for num in odd:
    if num <= 1:
        continue
    
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)

print("Prime numbers among them:", primes)
