# Pseudocode
# 1. Create a new list using 2 old list
# 2. From list 1, take odd numbers
# 3. From list 2, take even numbers
# 4. Return new list

number_list_a = [12, 13, 20, 0, 4,]
number_list_b = [5, 9, 20, 0, 5, 8]

def number_list_ab(number_list_a, number_list_b):
    merged_list = []

    for num in number_list_a:
        if num % 2 != 0:
            merged_list.append(num)

    for num in number_list_b:
        if num % 2 == 0:
            merged_list.append(num)

    return merged_list


print("Your new list:", number_list_ab(number_list_a, number_list_b))