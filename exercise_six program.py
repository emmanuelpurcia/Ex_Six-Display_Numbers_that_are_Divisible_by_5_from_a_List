# Hello! This program displays the numbers which are divisible by 5 based from a given list.

# pseudocode

# List of the Given Numbers
num_list = [10, 20, 33, 46, 55]
print("The Given list are:", num_list)

# Displays Numbers Divisible by 5
print('And this are the numbers that are Divisible by 5: ')
for num in num_list:
    if num % 5 == 0:
        print(num)
        