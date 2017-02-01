# This is the 4th step of hw4
# clustering the wordcount vectors using k-means
# input: vectors.txt
# output: output.txt

from sklearn.cluster import KMeans, MiniBatchKMeans
import numpy as np
import time

with open("vectors.txt", "r") as infile,open("wordcount.txt", "r") as wc, open("output.txt", "w") as output:
    num_cluster= 10
    vectors= []
    #trial= 2000
    #count= 0
    # vectors are read in from file, so in string format
    # requires pre-processing
    words= []
    i= 0
    for line in wc:
        line= line.replace("\n","")
        words.append(line)
        i += 1
        if i == 500:
            break
    for line in infile:
        newline= []
        line= line[1:len(line)-2]
        line= line.split(",")
        for l in line:
            l= int(l)
            newline.append(l)
        vectors.append(newline)
        #if count > trial:
           # break
        #count += 1

    #km= KMeans(n_clusters= num_cluster, random_state=0).fit(vectors)
    # setting up parameters for minibatch kmeans method
    batch_size = 45
    np_vec= np.array(vectors)
    print(len(vectors))
    mbk = MiniBatchKMeans(init='k-means++', n_clusters=num_cluster, batch_size=batch_size,n_init=10, max_no_improvement=10, verbose=0)
    t0 = time.time()
    mbk.fit(vectors)
    t_mini_batch = time.time() - t0
    print("Clustering takes %s" % str(t_mini_batch))
    #output.write("%s\n" % str(km.cluster_centers_))
    #print(km.cluster_centers_)
    #print(km.labels_)
    #output.write("The labeling is as below:\n")
    #output.write("%s\n" % str(mbk.cluster_centers_))
    #output.write("=======================================\n")
    output.write("The %s k-means centers are:\n" % str(num_cluster))
    i= 1
    for center in mbk.cluster_centers_:
        output.write("======== Center # %s:\n" % str(i))
        output.write("%s\n" % str(center))
        i += 1

    output.write("=======================================\n")
    for i in range(0,num_cluster):
        cluster= []
        fv= []
        wordcount= 500*[0]
        indices = [j for j, x in enumerate(mbk.labels_) if x == i]
        #print(type(indices))
        #print(indices)
        for j in indices:
            cluster.append(vectors[j])
            wordcount= [a+b for a,b in zip(wordcount,vectors[j])]
        #npcluster= np.matrix(cluster)
        #print(npcluster.shape)
        #wordcount= npcluster.sum(axis=0)
        for j in range(0,len(wordcount)):
            fv.append([wordcount[j],j])
        fv= sorted(fv, key= lambda x: x[0], reverse=True)
        output.write("========Representing words for cluster %s:\n" % str(i+1))
        for k in range(0,5):
            if k == len(fv):
                break
            output.write("== Word # %s:\n" % str(k+1))
            output.write("%s" % str(words[fv[k][1]]))
            output.write("  ,  %s\n" % str(fv[k][0]))
        

    
