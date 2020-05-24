import json
from scipy.sparse import *
from scipy import *
from sklearn.metrics.pairwise import *

vectors = load_npz("vectors.npz")
docs, features = vectors.get_shape()
print(docs,features)

arraay = vectors.toarray()
#print(arraay[:10])
print(len(arraay))
similarities = cosine_similarity(arraay)
print("done")
print(similarities.shape)

#print(similarities)

for i in range(docs):
    similarities[i,i] = -1

one_sim = argmax(similarities,1)
i=0
for one in one_sim:
    similarities[i,one] = -1
    i =i+1
two_sim = argmax(similarities,1)
print(on_sim,two_sim)
print(len(one_sim),len(two_sim))


print(argmax(similarities,1))




