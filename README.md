Attempt 1: Movie Title as Key w/ Linked List
The hash function for this attempt was a basic character counter. The hash() method added up the Unicode values for each character in the string. 


Attempt 2: Movie Title as Key w/ Linear Probing
The results of this test were such:
Hash Table Results 
    Buckets: 15000 
    Total entries: 11309 
    Total Collisions: 54250752 
    Time elapsed: 7.485205 seconds
The problem with this is that there are 4000 entries missing, and I have a sneaking suspicious how that happened. 

After this, I decided to go for something more unique: quotes. This took 4 seconds longer, but had more unique values filled out:
    Buckets: 15000 
    Total entries: 14891 
    Total Collisions: 91702029 
    Time elapsed: 12.32598
Weird. 