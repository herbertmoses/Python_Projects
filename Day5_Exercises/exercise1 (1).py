def return_different_values(a, b, c):

    a_sum = a + b + c
    a_list = [a, b, c]

    if a_sum > 15:
        return max(a_list)
    elif a_sum < 10:
        return min(a_list)
    else:
        a_list.sort()
        return a_list[1]


print(return_different_values(3, 2, 7))