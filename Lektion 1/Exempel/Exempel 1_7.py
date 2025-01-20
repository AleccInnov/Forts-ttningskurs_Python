# while-loop som använder både continue och break

i = 0
while i < 10:
    i += 1
    if i == 3:
        print("Skipping 3")
        continue  # Skip the rest of the loop and continue with the next iteration

    if i == 8:
        print("Breaking at 8")
        break  # Exit the loop when i equals 8

    print("Current value of i:", i)
