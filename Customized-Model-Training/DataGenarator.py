import random


def point_data_generate(num, r):
    # with args default settings
    x_data = [random.randint(0, r) for _ in range(num)]
    y_data = [random.randint(0, r) for _ in range(num)]
    return x_data, y_data

