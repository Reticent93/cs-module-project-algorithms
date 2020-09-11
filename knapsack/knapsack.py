#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity, weights):
    # Your code here
    cache = [[0] * (capacity + 1)] * (len(items) + 1)

    for total_items in range(0, len(items) + 1):
        for max_weight in range(0, capacity + 1):
            current_item = total_items - 1

            if total_items == 0 or max_weight == 0:
                cache[total_items][max_weight] = 0
            elif weights[current_item] > max_weight:
                cache[total_items][max_weight] = cache[total_items - 1[max_weight]]
            else:
                with_item = items[current_item] + cache[total_items - 1][max_weight - weights[current_item]]
                without_item = cache[total_items - 1[max_weight]]
                cache[total_items][max_weight] = max(with_item, without_item)

    return cache[len(items)][capacity]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
