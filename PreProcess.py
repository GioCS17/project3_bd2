import face_recognition as fc
import os
import time

path_files=[]
vector_files=[]
len_array=0
dim_vec=0

path_dataset_vec="./files/vec.txt"
path_dataset_paths="./files/paths.txt"

def preprocess(path_photos):
    print("PreProcessing Photos ...")
    #check if file exist
    if os.path.isfile(path_dataset_vec):
        return


    file_vec=open(path_dataset_vec,"w")
    file_path=open(path_dataset_paths,"w")
    begin=time.time()
    for r,d,f in os.walk(path_photos):
        for file in f:
            path=r+'/'+file
            img=fc.load_image_file(path)
            vec=fc.face_encodings(img)
            if len(vec)==0:
                continue
            new_vec=','.join(str(e) for e in vec[0])
            file_vec.write(new_vec+'\n')
            file_path.write(path+'\n')
            #path_files.append(path)
            #vector_files.append(vec)

    file_vec.close()
    file_path.close()
    print("Time Char Vec. is::",time.time()-begin)

def load_var():
    print("Loading Characteristic Vector ...")
    global len_array
    global dim_vec
    begin=time.time()
    file_vec=open(path_dataset_vec,"r")
    file_path=open(path_dataset_paths,"r")
    for line in file_vec.readlines():
        new_vec=[float(e) for e in line.split(',')]
        vector_files.append(new_vec)
        len_array+=1
    dim_vec=len(vector_files[0])
    print("DIM::",dim_vec)
    for line in file_path.readlines():
        path_files.append(line)

    print("Time Upload is::",time.time()-begin)
    print("Uploaded files::",len_array)

