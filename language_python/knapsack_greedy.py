from knapsack_data_abstract import *


"""
The first approach to solving the knapsack problem is the so called greedy
approach.
"""

def greedy(items, constraint, key_function):
    """
    items => [Item_Objects]
    constraint => > 0
    Key_function => mapping of elements to items (here is what we mean by best)
    """
    items_copy = sorted(items, key=key_function, reverse=True)
    # items_copy sorted best --> worst
    result = [] # acts as the "Knapsack"
    total_value, total_weight = 0.0, 0.0

    for item in range(len(items_copy)):
        if (total_weight + items_copy[item].get_weight()) <= constraint:
            result.append(items_copy[item])
            total_weight += items_copy[item].get_weight()
            total_value += items_copy[item].get_value()
    return result, total_value

"""
*****************************************************************************
TEST UNITS
*****************************************************************************
"""

def test_greedy(items, constraint, key_function):
    # call greedy algorithm
    taken, value = greedy(items, constraint, key_function)
    # format results
    print(f'Total value of the items taken is {value}\n')
    for item in taken:
        print(item)

def test_greedy_multi(items, constraint):
    print('Greedy by value\n')
    test_greedy(items, constraint, Item.get_value)
    print('Greedy by weight\n')
    test_greedy(items, constraint,
                # Lambda to get the inverse of get_weight() 
                lambda x: 1/Item.get_weight(x))
    print('Greedy by <value - weight> ratio\n')
    test_greedy(items, constraint, Item.get_value_weight_ratio)


if __name__ == '__main__':
    items = ['ball', 'watch', 'hat', 'bat', 'TV', 'couch', 'jacket']
    values = [10, 100, 10, 15, 450, 500, 125]
    weights = [1, 0.3, 0.2, 3, 123, 1000, 1.5]
    collection = build_items(items, values, weights)
    test_greedy_multi(collection, 850)
