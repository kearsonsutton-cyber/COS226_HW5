# Kearson Sutton
# COS226
# HW6: Hash Function
#
# The following hash table is made by putting values into bins between 0-9. This is, understandably, a very bad way to set up a hash table. However, it's also pretty fast!

import csv
import time

class HashTable:
    def __init__(self):
        self.buckets = 150
        self.data = {}
        self.size = 0

        # Statistics Variables
        self.collisions = 0

    def __str__(self):

        result = "Hash Table Results \n"
        result += f"Buckets: {self.buckets} \n"
        result += f"Total entries: {self.size} \n"
        result += f"Collisions: {self.collisions} \n"

        return result

    def hash(self, key):
        

        hash_value = 0
        for char in key:
            hash_value += ord(char)     # Add ASCII values
        return hash_value % self.buckets

    def append(self, key, value):
        hashed_key = self.hash(key)
        new_node = Node(key, value)

        # Scenario A: Bucket empty, create first node
        if hashed_key not in self.data:
            self.data[hashed_key] = new_node
            self.size += 1
            return
        
        else:
            current = self.data[hashed_key]
            while current:
                # If the key exists, update value
                if current.key == key:
                    current.value = value
                    return

                current = current.next

            new_node.next = self.data[hashed_key]
            self.data[hashed_key] = new_node

            self.size += 1                              # Increase size
            self.collisions += 1        # +1 Collision each time it goes to next node over


    def delete(self, key):
        hashed_key = self.hash(key)

        if hashed_key not in self.data:
            return False            # No need to go through this if it doesnt exist.

        current = self.data.get(hashed_key)
        previous = None

        # Find node to delete
        while current:
            if current.key == key:
                if previous is None:    # At the head of the bucket
                    if current.next:
                        self.data[hashed_key] = current.next    # Make next value replace current
                    else:
                        del self.data[hashed_key]
                else:
                    # Delete middle/tail
                    previous.next = current.next

                self.size -= 1
                return True

            previous = current
            current = current.next

        return False

    
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def main():
    hash_table = HashTable()
    row_number = 0

    # Get table values
    print('Starting hash population now...')

    start_time = time.perf_counter()        # Record time start

    with open('MOCK_DATA.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for movie in reader:
            row_number += 1
            _key = f"{movie['quote']}_{row_number}" 

            hash_table.append(_key, movie)
        
    end_time = time.perf_counter()

    duration = end_time - start_time

    print(f'Took {duration:.6f} seconds to complete')

    print(hash_table)

if __name__ == "__main__":
    main()