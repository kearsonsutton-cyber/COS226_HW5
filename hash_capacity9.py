# Kearson Sutton
# COS226
# HW6: Hash Function
#
# The following hash table is made by putting values into bins between 0-9. This is, understandably, a very bad way to set up a hash table.

import csv
import time

class HashTable:
    def __init__(self):
        self.buckets = 10
        self.data = {}
        self.size = 0

        # Statistics Variables
        self.memory_use = 0
        self.collisions = 0

    def __str__(self):
        result = "Hash Table Results \n"

        # for index, entry in self.data.items():
        #     current = entry

        #     while current:
        #         result += f'{index}: {current.key} : {current.value}\n'
        #         current = current.next

        result += f'Maximum Buckets: {self.buckets}'
        result += f'Amount of buckets filled: {self.unused_buckets()}'


        return result


    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)     # Add ASCII values
        return hash_value % self.buckets

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
                self.collisions += 1        # +1 Collision
                self.memory_use += 1      # +1 memory each time it goes to next node over

            new_node = Node(key, value)
            new_node.next = self.data[hashed_key]
            self.data[hashed_key] = new_node
            self.size += 1                              # Increase size
            self.memory_use += 1                        # Append is O(1)

    def search(self, key):
        hashed_key = self.hash(key)
        current = self.data[hashed_key]

        while current:
            if current.key == key:
                return current.value
            current = current.next
            self.memory_use += 1 # Searching is O(1), do so each loop

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

    # Calculates how many buckets were used; if all buckets are filled, the expected value is 0.
    def unusued_buckets(self):
        count = 0

        for bucket in self.data.values():
            if bucket is None:
                count += 1

        return count

    def waste_percentage(self):
        return (self.unused_buckets() / self.capacity) * 100

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
            hash_table.size += 1
        
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f'Took {duration:.6f} seconds to complete')

    write_to_csv(hash_table.data)
    # print(hash_table)

# Write Hash Table Values to a CSV to check if my output is valid
# Result should be:
# bucket/key : value
def write_to_csv(data):
    file = 'OUTPUT_DATA.csv'
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Key", "Value"] )   # First Row
        for key, value in data.items():
            writer.writerow([key, value])

if __name__ == "__main__":
    main()