def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number =  3 * number + 1
        print(number)
        return number


print("Enter number: ")
while True:
    try:
        a = int(input())
        break
    except ValueError:
        print('Error: Introduce a Number.')

while collatz(a) != 1:
    a=collatz(a)
