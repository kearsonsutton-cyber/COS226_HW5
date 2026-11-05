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
        self.memory_use = 0s
        self.collisions = 0

    def __str__(self):
        result = "Hash Table Results \n"
        result += f"Buckets: {self.buckets} \n"
        result += f"Total entries: {self.size} \n"
        result += f"Collisions: {self.collisions} \n"
        result += f"Memory Usage: {self.memory_use} \n"


        # Add Each Bucket to the CSV
        # Index goes from 0-Buckets, and fills in whether something exists there or not.

        for index in range(self.buckets):
            result += f"Bucket {index}: \n"

            if index not in self.data:
                result += "\t Empty"
                continue

            current = self.data[index]

            while current:
                result += f"\t [{current.key}: {current.value}]"
                current = current.next

                if current:
                    result += " -> \n"

            result += "\n"

        return result

    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)     # Add ASCII values
        return hash_value % self.buckets

    def append(self, key, value):
        hashed_key = self.hash(key)

        for i in range(self.buckets):
            current_index = (hashed_key + 1) % self.buckets
            entry = self.data[current_index]

            # Case 1: Bucket is Empty
            if entry is None:
                entry = (key, value)
                self.size += 1
                return

            # Case 2: Existing key is there
            if entry[0] == key:
                entry = (key, value)
                return

            self.collisions += 1

    def search(self, key):
        hashed_key = self.hash(key)
        current = self.data.get(hashed_key)

        while current:
            if current.key == key:
                return current.value
            current = current.next
            self.memory_use += 1 # Searching is O(1), do so each loop

        # If nothing was found, key does not exist!
        return None

    def delete(self, key):
        hashed_key = self.hash(key)
        current = self.data.get(hashed_key)
        previous = None

        # Find node to delete
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.data[hashed_key] = current.next
                    self.size -= 1          # Node removed.
                return True

            previous = current
            current = current.next  # Current is set for next node in list

        # Key went unfound:
        return False


    # Calculates how many buckets were used; if all buckets are filled, the expected value is 0.
    def unusued_buckets(self):
        return self.buckets - len(self.data)

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
        
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f'Took {duration:.6f} seconds to complete')

    write_to_csv(hash_table)
    # print(hash_table)

# Write Hash Table Values to a CSV to check if my output is valid
# Result should be:
# bucket/key : value
def write_to_csv(data):
    file = 'OUTPUT_DATA.csv'
    with open(file, "w", newline="", encoding="utf-8") as f:
        f.write(str(data))

if __name__ == "__main__":
    main()