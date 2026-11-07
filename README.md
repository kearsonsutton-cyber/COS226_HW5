Attempt 1: Movie Title as Key w/ Linked List
    Buckets: 10 
    Total entries: 11309 
    Collisions: 11299 
    Time elapsed: 0.298913 seconds
The hash function for this attempt was a basic character counter. The hash() method added up the Unicode values for each character in the string. This one was exceptionally quick, though I imagine that searching through each bucket will take quite some time. 


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
    Time elapsed: 12.32598 seconds
Weird. I am realizing now that the issue is a lack of uniqueness in keys... I will have to fix this!!

Attempt 3: Good Hash Function, Movie Title w/ Linked List
