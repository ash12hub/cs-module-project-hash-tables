class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.number_of_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.number_of_items / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        encode_bytes = key.encode()
        current_sum = 0
        for byte in encode_bytes:
            current_sum += byte

        c = 0
        djb2_hash = 5381
        for i in range(current_sum ):
            c = i
            djb2_hash = ((djb2_hash << 5) + djb2_hash) + c
        return djb2_hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        
        index = self.hash_index(key) % self.capacity
        
        if self.hash_table[index] is None:
            self.hash_table[index] = HashTableEntry(key, value)
            self.number_of_items += 1
        else:
            current_node = self.hash_table[index]
            while current_node is not None:
                if current_node.key == key:
                    current_node.key = key
                    current_node.value = value
                    break
                if current_node.next == None:
                    current_node.next == HashTableEntry(key, value)
                    self.number_of_items += 1
                    break
                current_node == current_node.next


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        warning = "Key Not Found"
        index = self.hash_index(key)
        current_entry = self.hash_table[index]
        if scurrent_entry == None:
            print(warning)
        elif current_entry.key == key:
            self.hash_table[index] == current_entry.next
            self.number_of_items -= 1
        else:
            previous_entry = current_entry
            current_entry = current_entry.next
            while current_entry is not None:
                if current_entry.key == key:
                    previous_entry.next = current_entry.next
                    self.number_of_items -= 1
                    return
                previous_entry = current_entry
                current_entry = current_entry.next
            print(warning)



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.hash_table[index] == None:
            return None
        else:
            current_node = self.hash_table[index]
            while current_node is not None:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        old_table = self.hash_table
        self.hash_table = [None] * new_capacity

        for entry in old_table:
            current_entry = entry
            while current_entry is not None:
                self.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
