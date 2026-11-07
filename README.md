**Attempt 1: Movie Title as Key w/ Linked List**
    Buckets: 10 
    Total entries: 11309 
    Collisions: 11299 
    Time elapsed: 0.298913 seconds
The hash function for this attempt was a basic character counter. The hash() method added up the Unicode values for each character in the string. This one was exceptionally quick, though I imagine that searching through each bucket will take quite some time. 

**Attempt 2: Movie Title as Key w/ Linear Probing**
The results of this test were such:
    Buckets: 15000 
    Total entries: 11309 
    Total Collisions: 54250752 
    Time elapsed: 7.485205 seconds
The problem with this is that there are 4000 entries missing, and I have a sneaking suspicion on how. Another big problem with this version of the test is that I had 54,250,752 collisions, which is nearly 24 times the amount of the list. I also decided to run through another attempt with movie quotes before changing anything, to see if the issue is in the lack of uniqueness in keys.

**Attempt 3: Movie Quotes w/ Linear Probing**
    Buckets: 15000 
    Total entries: 14891 
    Total Collisions: 91702029 
    Time elapsed: 12.32598 seconds
This took 4 seconds longer and had fewer entries missing, but still not ideal. There were also even more collisions with this time: 91,702,029. I am going to implement a way to adjust the value being put in as each movie's key (adding _(row_number) to it). 

**Attempt 4: Movie Quote w/ Linked List**
    Buckets: 10 
    Total entries: 15000 
    Collisions: 14990 
    Time elapsed: 0.365189 seconds
After making this implementation, I successfully get 15,000 total entries with each run of the file. However, the ~0.66 seconds added to the elapsed time is likely being lost to movie quotes, it is clear that ~0.68 seconds is being lost to editing movie quotes. Notably, there are very few collisions happening. By far, the linked list is proving to be the fastest of the two, with minimal collisions happening. This is likely because each data entry can, at most, run into [Max # of Data - Current Data Entry Index] other entries in each bucket. 

Another issue this is going to run into is that it also loops through the set of titles/quotes that I have stored in each iteration to check for duplicates. 

**Attempt 5: Movie Title w/ Linear Probing**
    Buckets: 15000 
    Unused buckets: 0
    Total entries: 15000 
    Total Collisions: 87004276 
    Time elapsed: 11.840517 seconds
15,000 buckets and 15,000 entries means I successfully got unique keys and unique buckets for each data entry in this table. The trend of high collisions continues, though slightly less than the attempt that didn't get all the entries in. It also shaves off about 0.5 seconds from the time complexity. I am now going to use Quotes and see how that changes the speed and collisions:

    Total Collisions: 92756776 
    Time elapsed: 12.419736 seconds


**Attempt 6: Movie Quotes w/ Linear Probing**
    Buckets: 15000 
    Unused buckets: 0
    Total entries: 15000
    Total Collisions: 92756776 
    Time elapsed: 12.419736 seconds

Well, that isn't efficient at all. Probably because the quotes can be much longer. Let's see how long it takes with the Linked List version.


**Attempt 7: Movie Quotes w/ Linked List**
    Buckets: 10 
    Total entries: 15000 
    Collisions: 14990 
    Time elapsed: 0.371376 seconds

The only thing I changed here was removing a print statement, and yet the algorithm's time complexity got longer. I find this curious, but I am unsure how to solve the problem. 


I will next adapt my hash function so that the handling of repeat values isn't done inside of main. I doubt it will fix anything yet, but I want to implement more hashing logic to see if that slows things down...

