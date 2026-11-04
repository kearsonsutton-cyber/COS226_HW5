# Kearson Sutton
# COS226
# HW6: Hash Function

import csv

class HashTable:
    def __init__(self):
        self.data = {}

    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)     # Add ASCII values
        return hash_value % len(self.data)

    def append(self, data):
        hashed_key = self.hash(data.key)
        if hashed_key not in self.data:
            self.data[hashed_key] = {}
        self.data[hashed_key][data] = value

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
        self.key = title                # Key is set to title

def main():
    hash_table = HashTable()
    # Get table values
    with open('MOCK_DATA.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_entry = MovieQuote(row['movie_title'], row['quote'], row['genre'],
                                   row['release_date'], row['director'], row['box_office_revenue'],
                                   row['rating'], row['duration'], row['production_company'])
            hash_table.append(new_entry)

if __name__ == "main":
    main()