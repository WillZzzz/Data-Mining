Project Requirements:

1. Identify all the unique words that appear in the \review/text" field of the reviews. Denote
the set of such words as L.

2.  Remove from L all stopwords in \Long Stopword List" from http://www.ranks.nl/stopwords.
Denote the cleaned set as W.

3. Count the number of times each word in W appears among all reviews (\review/text"field)
and identify the top 500 words.

4. Vectorize all reviews (\review/text"field) using these 500 words.

5. Cluster the vectorized reviews into 10 clusters using k-means. You are allowed to use any
program or code for k-means (Weka has k-means too). This will give you 10 centroid
vectors.

6. From each centroid, select the top 5 words that represent the centroid (i.e., the words with
the highest feature values)

*************************************************************************************************
Code Instruction:

1. Use bash command to extact the text reviews from the original file foods.txt.

2. Run cleaning.py to delete the stop words based on longstopword.txt from the reviews. So the output will be text reviews without meaningless words.

3. Run wordcount.py to count the occurences of each word and pick the top 600 frequent words. Delete the numbers and meaningless symbols like "\br".

4. Run vectorizing.py to vectorize the reviews by the top 500 frequent words. 

5. Run clustering.py to perform a MiniBatch K-Means to cluster the reviews. Output is the centers and 5 representinng reviews for each 

*************************************************************************************************
Source of Data:

Reviews from Amazon.com:
http://snap.stanford.edu/data/web-FineFoods.html

Long stopword list:
http://www.ranks.nl/stopwords


