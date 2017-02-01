# This is the first step of hw4
# cleaning the reviews by wiping out stop words
# input: reviews.txt
#        longstopwords.txt
# output: cleanreviews.txt
import re

with open("reviews.txt", "r") as infile, open("longstopwords.txt", "r") as stopwd, open("cleanreviews.txt", "w") as outfile:
    content= infile.readlines()
    #stpword= stopwd.readlines()
    stpword= []
    for line in stopwd:
        #print(line.strip("\n"))
        #print(type(line))
        stpword.append(line.strip("\n"))
    #print(stpword)
    m= len(content)
    output= []
    for i in range(0, m):
        review= content[i]
        review= review[13::]
        split= re.findall(r"[\w']+", review)
        set_split= set(split)
        split= list(set_split)
        split= [s.lower() for s in split]
        new_split= []
        for j in range(0, len(split)):
            if split[j] not in stpword:
                #split.remove(split[j])
                new_split.append(split[j])
            #if j == len(split):
                #break
        outfile.write("%s\n" % new_split)
        if i%1000 == 0:
            print("At review:", i)
        #output.append(split)
    
