# 
# Do not just send in the title / quote, put in the whole movie as an object
#
# Remove the search function.
# Search based on movie title OR quote.

def createMovie(title, genre, rating, box_office_revenue, director, quote):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating,
        "box_offce_revenue": box_office_revenue,
        "director": director,
        "quote": quote
    }

    return movie

movieToAdd = createMovie("Holy", "Romcom", "E", "1000", "Robbie Williams", "Hellothere.")

# Hash Function does NOT modulo.
# 15000 size

key = hashify(movieToAdd["title"])
key = key % sizeOfTable
key = hashify(movieToAdd["quote"])