import random


def throw_die():
    # random.randrange(a, b) geeft een getal tussen a (inclusief) en b (exclusief)
    return random.randrange(1, 7)


def probability_of_sum_higher_than(dice_count, minimum_sum, samples):
    count = 0

    for _ in range(0, samples):
        sum = 0

        for _ in range(0, dice_count):
            sum += random.randrange(1, 7)

        if sum > minimum_sum:
            count += 1

    return count / samples
