# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # use the hash_mod to get the position in the array
        position = self._hash_mod(key)
        # make a node with the new value
        new_node = LinkedPair(key, value)
        # get the item at position
        current_node = self.storage[position]

        # if the current position is empty insert
        if not current_node:
            self.storage[position] = new_node
        else:
            # transverse the linked list
            while current_node:
                # check if keys match and update it's value if they match
                if self._hash(key) == self._hash(current_node.key):
                    current_node.value = value
                    return
                # check if the next in the list is empty
                if not current_node.next:
                    # if empty insert the new node there
                    current_node.next = new_node
                    return
                # else move current node to the next node
                current_node = current_node.next

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # get postion for the item
        position = self._hash_mod(key)

        # current item at position
        current_item = self.storage[position]

        # tranverse the linked list
        while current_item:
            # compare the keys
            if self._hash(key) == self._hash(current_item.key):
                # get the next item
                next_item = current_item.next
                # set the next item to the current position
                self.storage[position] = next_item
                return key
            # move to the next item
            current_item = current_item.next

        print('Warning: Key Not Found')
        return None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get the position in the array
        position = self._hash_mod(key)
        hashed_key = self._hash(key)

        # get the node at the current position
        current_node = self.storage[position]

        # Tranverse the linked list
        while current_node:
            # compare the key of the node in the linked list with the hashed key
            if self._hash(current_node.key) == hashed_key:
                # return the value of the current node
                return current_node.value
            # move on to the next node
            current_node = current_node.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
