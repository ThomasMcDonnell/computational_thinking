from knapsack_data_abstract import *


"""
Brute force algorithm to explore all possible combinations of items in order to
pick the most optimal solution.
Here we have a search tree implamentation whereby nodes represent the knapsack
with different combinations of items.

* 1.The tree is built top down starting with the root and the first element is
    selected from the items_to_be_considered.
* 2.The left child denotes the consequences of taking an item the right
    explores not taking that item.
* 3.We then recursively reapply the process to the non left childern.
* 4.We than evaluate and choose the node with the higest value within the set
    constraints.

*****************************NOTE*********************************************
We do not actually build the search tree instead the local variable result
records the best solution so far.
"""
def max_value(items_to_consider, available_weight):
    if items_to_consider == [] or available_weight == 0:
        result = (0, ())
    elif items_to_consider[0].get_weight() > available_weight:
        #Explore right branch only
        result = max_value(items_to_consider[1:], available_weight)
    else:
        next_item = items_to_consider[0]
        #Explore left branch
        with_value, with_to_take = max_value(items_to_consider[1:],
                                     available_weight - next_item.get_weight())
        with_value += next_item.get_value()
        #Explore right branch
        without_value, without_to_take = max_value(items_to_consider[1:],
                                                   available_weight)
        #Choose better branch
        if with_value > without_value:
            result = (with_value, with_to_take + (next_item,))
        else:
            result = (without_value, without_to_take)
    return result


"""
************************************TEST UNIT ******************************************
"""


def test_max_value(items, constraint, print_items=True):
    value, taken = max_value(items, constraint)
    print(f'Total value of items take is {value}')
    if print_items:
        for item in taken:
            print(f'{item}')


if __name__ == '__main__':
    items = ['ball', 'watch', 'hat', 'bat', 'TV', 'couch', 'jacket']
    values = [10, 100, 10, 15, 450, 500, 125]
    weights = [100, 100, 200, 300, 1230, 1000, 100]
    collection = build_items(items, values, weights)
    test_max_value(collection, 750)
