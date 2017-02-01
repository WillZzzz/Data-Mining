# This is the 3rd step of hw4
# vectorizing reviews using the top 500 frequent words
# input: wordcount.txt
#        cleanreviews.txt
# output: vectors.txt

with open("wordcount.txt", "r") as infile,open("cleanreviews.txt", "r") as reviews, open("vectors.txt", "w") as outfile:
    topwords= []
    # set how many top words we need
    top= 500
    i= 0
    # wordcount.txt contains the top words only, in strings,
    # so proper pre-processing are needed, for example
    # getting rid of the "s and 's
    for line in infile:
        #line= line.replace("\\","")
        line= line.replace("\n","")
        #print(line)
        topwords.append(line)
        i += 1
        if i == top:
            break
    #print(topwords[0:10])
    #print(topwords[4])
    #print(topwords[4] == '"it\'s"')
    m= len(topwords)
    content= reviews.readlines()
    n= len(content)
    # vectors[] will hold the vectors
    vectors= []
    for i in range(0,n):
        # initialize the vector for each review
        v= 500*[0]
        cont= content[i]
        cont= cont[1:len(cont)-2]
        cont= cont.split(", ")
        for j in range(0,m):
            word= topwords[j]
            if word in cont:
                v[j]= 1
        vectors.append(v)
        outfile.write("%s\n" % v)
        if i%1000 == 0:
            print("At review:", i)
        
        
