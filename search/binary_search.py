numbers = list(range(1,1001))

target =int(input("target:"))
N = len(numbers)
L = 0
H = N-1
i = 0
while True:
    m = (H+L)//2 
    if target == numbers[m]:
        searched_number = numbers[m]
        iterationsi = i + 1
        break
    elif target>numbers[m]:
        L=m+1
    else:
        H=m-1
    i += 1

print(f"The searched number: {searched_number}\nNumber of iterations: {iterationsi}")

