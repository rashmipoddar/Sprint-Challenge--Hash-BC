#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length-1)

    """
    YOUR CODE HERE
    """

    for i in range(0, length):
        # print(tickets[i].source)
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    start = hash_table_retrieve(hashtable, "NONE")
    print(start)
    print(route)
    route[0] = start

    for j in range(1, length):
        value =  hash_table_retrieve(hashtable, route[j-1])
        if (j < length):
            route[j] = value

    print(route)

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
reconstruct_trip(tickets, 3)