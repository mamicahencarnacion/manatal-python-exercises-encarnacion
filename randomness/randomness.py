import random


def get_lottery_output():
    """
    :rtype: list
    :return: sorted list of 10 random numbers between 1 to 50
    """
    return sorted(random.sample(range(1, 51), 10))


if __name__ == "__main__":
    print(get_lottery_output())
