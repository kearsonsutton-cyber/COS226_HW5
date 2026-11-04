# Kearson Sutton
# COS226
# HW6: Hash Function

import csv
import time

class HashTable:
    def __init__(self, capacity=30):
        self.capacity = capacity
        self.data = {i: None for i in range(self.capacity)}
        self.size = 0

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
        return hash_value % self.capacity

    def append(self, key, value):
        hashed_key = self.hash(key)

        current = self.data[hashed_key]

        # Scenario A: Bucket empty, create first node
        if self.data[hashed_key] is None:
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
            self.size += 1

    def search(self, key):
        hashed_key = self.hash(key)
        current = self.data[hashed_key]

        while current:
            if current.key == key:
                return current.value
            current = current.next

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

class MovieQuote:
    def __init__(self, title, quote, genre, release_date,
                 director, box_office_revenue, rating,
                 duration, production_company):
        self.title = title
        self.quote = quote
        self.genre = genre
        self.release_date = release_date
        self.director = director
        self.box_office_revenue = box_office_revenue
        self.duration = duration
        self.production_company = production_company
        self.rating = rating

        # Key / Value Pair
        self.key = title                # Key is set to title
        self.value = quote              # Value is set as quote

        self.next = None

    def __str__(self):
        return f"""{self.title}, {self.release_date}
        Directed by {self.director} at {self.production_company}
        Quote: {self.value}"""

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
        counter = 0
        for row in reader:
            hash_table.append(row['movie_title'], row['quote'])
            counter += 1

            if counter >= 30:
                break
        
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f'Took {duration:.6f} seconds to complete')

    print(hash_table)

    

if __name__ == "__main__":
    main()