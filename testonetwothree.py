import sys
import random


def permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for e in permutations(s[:-1]):
            for i in range(len(e)+1):
                perms.append(e[:i] + s[-1] + e[i:])
        return perms


if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required \n')
    sys.exit(1)


# getting the word for permutations
x = input("word?\n")

# saving the result to a variable, making operations with it possible
z = permutations(x)

# printing randomly chosen 20 items from the list
print(random.sample(z, 20))
