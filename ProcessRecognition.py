from PreProcess import *
from Utils import *
from queue import PriorityQueue
from rtree import index

def knn(photo,k):
    print("Processing KNN methods ...")
    print("Input photo::",photo)
    img=fc.load_image_file(photo)
    vec=fc.face_encodings(img)
    if len(vec)==0:
        print("BAD Photo")
        return
    ans_pq1,ans_pq2=priorityqueue_knn(vec[0],photo,k)
    ans_rtree=rtree_knn(vec[0],photo,k)
    return  ans_pq1+ans_pq2+ans_rtree

def priorityqueue_knn(vec,photo,k):
    print("Processing Query KNN with Priority Queue")

    begin=time.time()
    pq_eucl=PriorityQueue()
    for i in range(len(vector_files)):
        dist_eucl=euclidean_distance(vector_files[i],vec)
        pq_eucl.put((dist_eucl,i))
    print("Time Priority Queue Euclidean Dist::",time.time()-begin)

    begin=time.time()
    pq_manh=PriorityQueue()
    for i in range(len(vector_files)):
        dist_manh=manhattan_distance(vector_files[i],vec)
        pq_manh.put((dist_manh,i))
    print("Time Priority Queue Manhattan Dist::",time.time()-begin)

    ans_eucl=[]
    ans_manh=[]
    while k:
        ans_eucl.append(pq_eucl.get()[1])
        ans_manh.append(pq_manh.get()[1])
        k-=1
    return ans_eucl,ans_manh

def rtree_knn(vec,photo,k):
    print("Processing Query KNN with RTree")
    p = index.Property()
    #p.dimensions=dim_vec
    p.dimension=128
    p.buffering_capacity=129
    p.dat_extension="data"
    p.idx_extension="index"
    idx=index.Index("rtree_index",properties=p)

    for i in range(len(vector_files)):
        idx.insert(i,tuple(vector_files[i]+vector_files[i]))

    begin=time.time()
    ans=list(idx.nearest(coordinates=tuple(vec+vec),num_results=k))
    print("Time in RTree::",time.time()-begin)

    return ans