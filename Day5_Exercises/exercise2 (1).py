def unrepited_letters(word):

    my_set = set()

    for letter in word:
        my_set.add(letter)

    my_list = list(my_set)
    my_list.sort()

    return my_list


print(unrepited_letters('pineapple'))