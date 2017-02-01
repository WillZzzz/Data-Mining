# This is the 2nd step for hw4
# counts the occurences of each word and select the most frequent ones
# input: cleanreviews.txt
# outpu: word+count.txt
from collections import Counter
from operator import itemgetter

with open("cleanreviews.txt", "r") as infile, open("word+count.txt", "w") as outfile:
    content= infile.readlines()
    counts= []
    counter_total= Counter([])
    m= len(content)
    for i in range(0,m):
        words= content[i]
        words= words[1:len(words)-2]
        words= words.split(", ")
        #words= [word.lower() for word in words]
        #print(words)
        counter= Counter(words)
        counter_total += counter
        if i%1000 == 0:
            print("At review:", i)

    #sorted_counts= sorted(counter_total, key=counter_total.get, reverse=True)
    # get the 600 most frequent words to leave some space for unexpected symbols
    sorted_counts= counter_total.most_common(600)
    i= 0
    for count in sorted_counts:
        #print("word:", count["word"],  "count:", count["count"])
        outfile.write("%s\n" % str(count))
        i += 1
        if i == 600:
            break;
    
