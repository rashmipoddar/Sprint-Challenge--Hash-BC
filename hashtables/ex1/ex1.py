#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)
    for j in range(0, length):
        value = hash_table_retrieve(ht, limit-weights[j])
        if value:
            if j > value:    
                return (j, value)
            else:
                return (value, j)

def print_answer(answer):
    print(answer)
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# get_indices_of_item_weights([4, 4], 2, 8)
# get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)
# get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7)