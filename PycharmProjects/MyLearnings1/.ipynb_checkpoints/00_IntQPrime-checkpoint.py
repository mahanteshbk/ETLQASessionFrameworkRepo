# Check Prime number

print("Enter a number")
num = int(input())
cnt = 0
inc = 1

while num>=inc:
    if num % inc == 0:
        cnt = cnt + 1
    inc = inc +1

if cnt == 2:
    print(num ,"is a PRIME number")
else:
    print(num,"is not a PRIME number")