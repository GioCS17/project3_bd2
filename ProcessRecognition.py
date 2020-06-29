from PreProcess import *
from Utils import *
from queue import PriorityQueue
from rtree import index

def knn(photo,k):
    print("Processing KNN methods ...")
    print("Input photo::",photo)
    img=fc.load_image_file(photo)
    vec=fc.face_encodings(img)
    print(vec)
    if len(vec)==0:
        print("BAD Photo")
        return
    #ans_pq=priorityqueue_knn(vec[0],photo,k)
    ans_rtree=rtree_knn(vec[0],photo,k)

def priorityqueue_knn(vec,photo,k):
    print("Processing Query KNN with Priority Queue")

    pq_eucl=PriorityQueue()
    for i in range(len(vector_files)):
        dist_eucl=euclidean_distance(vector_files[i],vec)
        pq_eucl.put((dist_eucl,i))

    pq_manh=PriorityQueue()
    for i in range(len(vector_files)):
        dist_manh=manhattan_distance(vector_files[i],vec)
        pq_manh.put((dist_manh,i))

    ans_eucl=[]
    ans_manh=[]
    while k:
        ans_eucl.append(pq_eucl.get()[1])
        ans_manh.append(pq_manh.get()[1])
        k-=1
    print(ans_eucl)
    return ans_eucl,ans_manh

def rtree_knn(vec,photo,k):
    print("Processing Query KNN with RTree")

    pq_eucl=PriorityQueue()
    for i in range(len(vector_files)):
        dist_eucl=euclidean_distance(vector_files[i],vec)
        pq_eucl.put((dist_eucl,i))

    pq_manh=PriorityQueue()
    for i in range(len(vector_files)):
        dist_manh=manhattan_distance(vector_files[i],vec)
        pq_manh.put((dist_manh,i))

    ans_eucl=[]
    ans_manh=[]
    while k:
        ans_eucl.append(pq_eucl.get()[1])
        ans_manh.append(pq_manh.get()[1])
        k-=1
    print(ans_eucl)
    return ans_eucl,ans_manh

