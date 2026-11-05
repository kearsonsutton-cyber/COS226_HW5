# Kearson Sutton
# COS226
# HW6: Hash Function

import csv
import time

class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = {}
        self.size = 0

        # Statistics Variables
        self.memory_use: 0

    def __str__(self):
        result = ""

        for index, entry in self.data.items():
            current = entry

            while current:
                result += f'{index}: {current.key} : {current.value}\n'
                current = current.next

        return result


    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)     # Add ASCII values
        return hash_value

    def append(self, key, value):
        hashed_key = self.hash(key)

        # Scenario A: Bucket empty, create first node
        if hashed_key not in self.data:
            self.data[hashed_key] = Node(key, value)
            self.size += 1
            return
        else:
        # Case 2: Collision!
            current = self.data[hashed_key]
            while current:
                # If the key exists, update value
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            new_node = Node(key, value)
            new_node.next = self.data[hashed_key]
            self.data[hashed_key] = new_node
            self.size += 1                              # Increase size
            self.memory_usage += 1

    def search(self, key):
        hashed_key = self.hash(key)
        current = self.data[hashed_key]

        while current:
            if current.key == key:
                return current.value
            current = current.next
            self.memory_usage += 1
            # Searching is O(1)

        # If nothing was found, key does not exist!
        return None

    def delete(self, key):
        hashed_key = self.hash(key)
        current = self.data[hashed_key]
        previous = None

        # Find node to delete
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.data[hashed_key] = current.next
                return True

            previous = current
            current = current.next  # Current is set for next node in list

        # Key went unfound:
        return False

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def main():
    hash_table = HashTable()



    # Get table values
    print('Starting hash population now...')
    start_time = time.perf_counter()        # Record time start
    with open('MOCK_DATA.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            hash_table.append(row['movie_title'], row['quote'])
        
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f'Took {duration:.6f} seconds to complete')

    print(hash_table)

    

if __name__ == "__main__":
    main()