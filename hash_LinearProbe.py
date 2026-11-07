# Kearson Sutton
# COS226
# HW6: Hash Function
#
# The following hash table is made by putting values into bins between 0-9. This is, understandably, a very bad way to set up a hash table.

import csv
import time

class HashTable:
    def __init__(self):
        self.buckets = 15000            # 15,000 entries
        self.data = {}
        self.size = 0                   # Unfilled

        # Statistics Variables
        self.collisions = 0

        # Linear Probing
        self.DELETED = object()        # Google said this was a good way of doing this.

    def __str__(self):
        result = "Hash Table Results \n"
        result += f"Buckets: {self.buckets} \n"
        result += f"Unused buckets: {self.buckets - self.size}\n"
        result += f"Total entries: {self.size} \n"
        result += f"Total Collisions: {self.collisions} \n"

        return result

    def hash(self, key):

        hash_value = 0

        for char in key:
            hash_value += ord(char)     # Add ASCII values

        return hash_value % self.buckets

    def append(self, key, value):

        hashed_key = self.hash(key)
        probes = 0                     
        # If probes == self.buckets, then we have gone through the whole list
        first_deleted = None
        new_node = Node(key, value)
        
        # Probe til bucket/same key
        while probes < self.buckets:
            current = self.data.get(hashed_key)

            # Empty bucket, yay! Let's go here.
            if current is None:

                if first_deleted is not None:
                    hashed_key = first_deleted
                
                self.data[hashed_key] = new_node
                self.size += 1
                return
            
            # Tombstone found!
            elif current is self.DELETED:
                if first_deleted is None:
                    first_deleted = hashed_key  # Could be useful later.
            
            # Key exists
            elif current.key == key:
                current.value = value
                return
            
            else:
                self.collisions += 1    # Since nothing happened, we have to move on, so this pass counts as a collision.
            
            hashed_key = (hashed_key + 1) % self.buckets    # Move to next index...
            probes += 1

        # Probed fully, tombstone was available though
        if first_deleted is not None:
            self.data[first_deleted] = new_node
            self.size += 1
            return
        
        raise OverflowError("Hash Table is full.")

    def delete(self, key):
        hashed_key = self.hash(key)
        probes = 0

        while probes < self.buckets:
            current = self.data.get(hashed_key)
            
            # Nothing was found at the key. 
            if current is None:
                return False
            
            # Overlook tombstone entries
            elif current is self.DELETED:
                pass
            
            # Found key! Woohoo!
            elif current.key == key:
                self.data[hashed_key] = self.DELETED
                self.size -= 1                 # -1 from array memory
                return True

            hashed_key = (hashed_key + 1) % self.buckets
            probes += 1
        return False

    # Calculates how many buckets were used; if all buckets are filled, the expected value is 0.
    def unused_buckets(self):
        return self.buckets - self.size


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # Stores row as a whole as the value. movie_title is put in as the key parameter, but will be changed between versions of this project. 

def main():
    hash_table = HashTable()
    titles = set()      # Keep track of duplicate titles
    #modified_titles = 0  # Keep track of titles that got adjusted
    row_number = 0      # Keep track of row to ensure that every title can be unique

    # Get table values
    print('Starting hash population now...')

    start_time = time.perf_counter()        # Record time start

    with open('MOCK_DATA.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for movie in reader:
            row_number += 1
            _title = movie['movie_title']

            # Check for duplicate
            if _title in titles:
                _title = f"{movie['movie_title']}_{row_number}"     # Modify movie_title accordingly. The actual movie itself goes in unchanged, though!
                # modified_titles += 1
            
            titles.add(_title)

            hash_table.append(_title, movie)                    # Putting in the movie object w/o changing ['movie_title'] directly
    
    #  print(f"Adjusted the values of {modified_titles} titles.")       Output: 3691!
        
    end_time = time.perf_counter()          # End time
    duration = end_time - start_time
    print(f'Took {duration:.6f} seconds to complete')

    write_to_csv(hash_table)

    print(hash_table)



# Write Hash Table Values to a CSV to check if my output is valid
def write_to_csv(data):
    file = 'OUTPUT_DATA_LinearProbe.csv'
    with open(file, "w", newline="", encoding="utf-8") as f:
        f.write(str(data))

if __name__ == "__main__":
    main()