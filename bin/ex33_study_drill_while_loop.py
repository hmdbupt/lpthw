def while_loop(variable, increment):
    i = 0
    numbers = []

    while i < variable:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)

        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

print("Start of while loop 10 with an increment of 5")
while_loop(10, 5)
print("End of while loop 10 with an increment of 5")

print("Start of while loop 20 with an increment of 2")
while_loop(20, 2)
print("End of while loop 20 with an increment of 2")
