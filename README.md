**Attempt 1: Movie Title as Key w/ Linked List**  

> Buckets: 10  
> Total entries: 11309  
> Collisions: 11299  
> Time elapsed: 0.298913 seconds  

The hash function for this attempt was a basic character counter. The hash() method added up the Unicode values for each character in the string. This one was exceptionally quick, though I imagine that searching through each bucket will take quite some time.   
  
**Attempt 2: Movie Title as Key w/ Linear Probing**    

The results of this test were such:  
> Buckets: 15000   
> Total entries: 11309   
> Total Collisions: 54250752   
> Time elapsed: 7.485205 seconds  

The problem with this is that there are 4000 entries missing, and I have a sneaking suspicion on how. Another big problem with this version of the test is that I had 54,250,752 collisions, which is nearly 24 times the amount of the list. I also decided to run through another attempt with movie quotes before changing anything, to see if the issue is in the lack of uniqueness in keys.  

**Attempt 3: Movie Quotes w/ Linear Probing**  

> Buckets: 15000   
> Total entries: 14891   
> Total Collisions: 91702029   
> Time elapsed: 12.32598 seconds  
  
This took 4 seconds longer and had fewer entries missing, but still not ideal. There were also even more collisions with this time: 91,702,029. I am going to implement a way to adjust the value being put in as each movie's key (adding _(row_number) to it). 

**Attempt 4: Movie Quote w/ Linked List**

> Buckets: 10  
> Total entries: 15000  
> Collisions: 14990   
> Time elapsed: 0.365189 seconds  
  
After making this implementation, I successfully get 15,000 total entries with each run of the file. However, the ~0.66 seconds added to the elapsed time is likely being lost to movie quotes, it is clear that ~0.68 seconds is being lost to editing movie quotes. Notably, there are very few collisions happening. By far, the linked list is proving to be the fastest of the two, with minimal collisions happening. This is likely because each data entry can, at most, run into [Max # of Data - Current Data Entry Index] other entries in each bucket. 

Another issue this is going to run into is that it also loops through the set of titles/quotes that I have stored in each iteration to check for duplicates. 

**Attempt 5: Movie Title w/ Linear Probing**  

> Buckets: 15000      
> Unused buckets: 0      
> Total entries: 15000     
> Total Collisions: 87004276       
> Time elapsed: 11.840517 seconds    

15,000 buckets and 15,000 entries means I successfully got unique keys and unique buckets for each data entry in this table. The trend of high collisions continues, though slightly less than the attempt that didn't get all the entries in. It also shaves off about 0.5 seconds from the time complexity. I am now going to use Quotes and see how that changes the speed and collisions:  

> Total Collisions: 92756776     
> Time elapsed: 12.419736 seconds    


**Attempt 6: Movie Quotes w/ Linear Probing**  

> Buckets: 15000     
> Unused buckets: 0    
> Total entries: 15000  
> Total Collisions: 92756776    
> Time elapsed: 12.419736 seconds  

Well, that isn't efficient at all. Probably because the quotes can be much longer. Let's see how long it takes with the Linked List version.  


**Attempt 7: Movie Quotes w/ Linked List**    

> Buckets: 10     
> Total entries: 15000     
> Collisions: 14990     
> Time elapsed: 0.371376 seconds    

The only thing I changed here was removing a print statement, and yet the algorithm's time complexity got longer. I find this curious, but I am unsure how to solve the problem. 


I will next adapt my hash function so that the handling of repeat values isn't done inside of main. I doubt it will fix anything yet, but I want to implement more hashing logic to see if that slows things down...

**Attempt 8: Movie Quote + Release Date**
I have decided to see what happened if I changed the linked and linear probe tables to have their keys be a quote + release date, to see if the time changed that much and if collisions went up or down. I was hoping that more unique datum would have reduced collisions...

Linked List Results  

> Buckets: 10     
> Total entries: 15000     
> Collisions: 14990     
> Time elapsed: 0.372346 seconds
 
Linear Probe  

> Buckets: 15000  
> Unused buckets: 0  
> Total entries: 15000   
> Total Collisions: 92797618   
> Time elapsed: 12.450382 seconds  

So I am still losing time. I will next attempt a new hashing method I found online called "double hashing", where the step size is decided by a secondary hash function. I figured it wouldn't hurt to try, and believe that anything is better than going +1, +1, +1 over all 15,000 entries. But maybe the computational load of figuring out a new hash key will be slow.

**Attempt 9: Movie Quote w/ Double Hashing Collision Resolution**  

> Buckets: 20011   
> Unused buckets: 5011  
> Total entries: 15000   
> Total Collisions: 90423   
> Time elapsed: 0.235455 seconds  
  
Double hashing significantly sped my linear probe up by 12 seconds. I am astonished! The number of total collisions shot down too, to the point that it is currently faster than my chaining method! I will now try to optimize the Linked List a bit more, but first, I will just make sure that the reason this worked so well isn't because I increased the number of buckets. Maxed buckets was capped at 15101 for this:  
  
> Buckets: 15101  
> Time elapsed: 0.337715  
> Total Collisions: 160795
  
A lot more collisions! I blame the significantly smaller table size, for sure. Let's see if making the buckets too big is a possibility?  
  
> Buckets: 35753  
> Time elapsed: 0.201462 seconds  
> Total Collisions: 75906  

Cool! Larger tables mean a faster algorithm, then; the ideal is to have more than necessary! I am going to apply this to the Linked List method next. 

**Attempt 10 Movie Quotes Linked List**

I accidentally deleted the README after I editing this section, so I am going to be brief. First, I tried to increase my bucket size to 50 and realized there was a connection between the bucket size and the number of collisions in my linked list; with 40 more buckets, collisions in my algorithm fell by 40. So I assumed that, if I chose 100 buckets as a start, the number of collisions would be 14900:

> Buckets: 100   
> Total entries: 15000   
> Collisions: 14900   
> Time elapsed: 0.106264 seconds  

And I was correct! So I was hoping to see if I could get collisions to 0 with 15000 buckets.

> Buckets: 15000  
> Total entries: 15000     
> Collisions: 12285   
> Time elapsed: 0.077023 seconds    

I expected to get diminishing returns when doing a massive bucket size for the linked list hash table, but was surprised by how fast it was. 0.077 seconds is crazy! However, it had 12285 collisions. It is unclear to me why, still. Around 2,000 buckets, the collisions stop going down for every bucket added. By 3,000 buckets the collisions are 12,372, and approach 12285 very very gradually. I found that to be interesting, and so I wanted to push it just a bit further before completing this project.

I set my buckets to 60,000 and found that it started to take a longer amount of time to do:

> Buckets: 60000   
> Total entries: 15000   
> Collisions: 12285   
> Time elapsed: 0.097537 seconds  

Clearly, there are diminishing returns for a linked list. Let's just see what happens for the Linear Probe, if it gets faster at 60,000 buckets...


> Buckets: 60000   
> Unused buckets: 45000  
> Total entries: 15000   
> Total Collisions: 74010   
> Time elapsed: 0.221572 seconds

I think it can get to a point where it's too big indeed; total collisions do not decrease by as much as when I had set it from 20011 to 35753. 

Clearly, there is a worst and best case for each of these algorithms. I believe that the hash table could be better utilized if it was a linked list that hashed the genre value of the movies, as that'd make it easier to find related movies to what I might want to watch next. But, this is a theoretical program.
