
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = 7
i=0
while True:
    if target==numbers[i]:
        searched_number=numbers[i]
        iterationsi=i+1
        break
    i+=1

print(f"The searched number: {searched_number}\nNumber of iterations: {iterationsi}\n")
