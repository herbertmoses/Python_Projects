def neighboring_zeros(*args):

    counter = 0

    for n in args:

        if counter + 1 == len(args):
            return False
        elif args[counter] == 0 and args[counter + 1] == 0:
            return True
        else:
            counter += 1

    return False


print(neighboring_zeros(0, 4, 0, 8, 1, 3, 9, 8, 0, 2, 0))