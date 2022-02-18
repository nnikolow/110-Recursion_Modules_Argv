import sys
import random


def permutations(sample):
    if len(sample) <= 1:
        yield sample
    else:
        for elem in permutations(sample[1:]):
            for i in range(len(sample)+1):
                yield elem[:i] + sample[0:1] + elem[i:]
        return sample


if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required \n')
    sys.exit(1)


# getting the word for permutations
x = input("word?\n")

# saving the result to a variable, making operations with it possible
z = list(permutations(x))

# printing randomly chosen 20 items from the list
print(random.sample(z, 20))
