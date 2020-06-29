# Project3_bd2
## Face recognition project

### Download Images:
- http://vis-www.cs.umass.edu/lfw/lfw.tgz

### Pre-Installation:
- Open CV: pip install opencv-python
https://pypi.org/project/opencv-python/
- Setup Tools: pip install setuptools 
https://pypi.org/project/setuptools/
- CMake: pip install cmake
https://pypi.org/project/cmake/
- DLib: pip install dlib
https://pypi.org/project/dlib/
- Face-recognition library: pip install face-recognition
https://pypi.org/project/face-recognition/
- RTree: pip install Rtree
https://pypi.org/project/Rtree/

### Division del Proyecto

#### Frontend
Para la implementación en frontend hacemos uso de las librerias **bulma css** para manejar el aspectos de las vistas de forma muy flexible y ligera, y **Vuejs** para el manejo de eventos y acciones desde las vista. Vuejs permite la comunicacion de las vistas con tu archivo o código javascript de forma muy fácil. Para la comunicación con el backend nos apoyamos de la libreria **axios**. Solo contamos con un archivo *index.html* para la carga de la imagen o foto por el usuario y una caja de texto para la consulta de los k más cercanas fotos. En esta misma vista, se podra obtener las k más cercanas fotos por la distancia **euclideana**, **manhattan** y con la ayuda de la estructura **RTree**. Al final del documento probar apreciar algunas imagenes que muestra como se encuentra index.html. 

#### Backend
Dentro de la implementación en backend se ha decidido dividir el procesamiento en el servidor en 4 archivos python cuales son los siguientes:

##### Utils
En este archivo de python se encuentran implementadas dos funciones, los cuales son los siguientes:
- **euclidean_distance**
Este función nos permite retornar las distancia euclideana entre dos vectores. 

- **manhattan_distance**
Este función nos permite retornar las distancia manhattan entre dos vectores. 

##### PreProcess
Dentro de este archivo de python se realiza la obtención del vectores caracteristico de cada imagen del dataset. Además, para un mejor uso futuro se genera dos archivos en el directorio **files**, el archivo **path.txt** y **vec.txt**.

Esta compuesto de dos funciones.
- **preprocess**
    En esta función se hace lectura que cada imagen del dataset.Asi mismo se genera el vector caracteristico de cada imagen para ahi mismo almacenarlo en el archivo **vec.txt**, tambien se almacena el path de la imagen en el archivo **paths.txt**.
- **load_var**
    En esta funcion se hace uso de los archivos generados en preprocess. Se hace lectura de cada uno de estos archivos y se almacenan en dos arreglos definidos por las variables **path_files** y **vector_files**. Estos dos arreglos se haran uso a los largo del proceso de face recognition.

##### ProcessRecognition
Este archivo engloba la parte del calculo de los k más cercanas imágenes. Se define una clase RTree la cual nos permitira hacer uso de la estructura para la obteción de las k imágenes mas cercanas.

Esta compuesto de las siguientes funciones:
- **build_tree**
Esta función completara la contruccion del Rtree insertando cada valor del arreglo **vector_files** al Rtree.

- **knn**
Esta función nos permitira hacer la búsqueda de las k imágenes mas cercanas, tanto por el uso de búsqueda secuencial con distancias euclideana y manhattan asi como el uso del Rtree. Dentro de la función se hace un llamado a las funciones **priorityqueue_knn** y **rtree_knn**. Tambien dentro de la función se genera el vector característico de la imagen en consulta.

- **priorityqueue_knn**
En esta funcion se genera dos arreglos siendo cada uno la respuesta para la consulta de knn tanto para la distancia euclideana como manhattan. Se hace uso de la estructura de python *PriorityQueue*.

- **rtree_knn**
En esta función ya se permite la obtención de las k imagenes cercanas con el uso de la estructura Rtree ya definida previamente.

##### Server
Esta archivo de python permitirá la comunicación entre el frontend o lado del cliente y el servidor.
Esta compuesto por:
- **index**
Esta función permitirá indicar que vista será la cual se inicie cuando se ejecute el servidor. En nuestro caso es **index.html**.
- **allowed_file**
Esta función permitirá validar los archivos ingresados, teniendo encuentra que solo se puede trabajar con 4 tipos de archivos (png,jpg,jpeg,gif).
- **build_rtree**
Luego de iniciado el servidor, se hace uso de esta función para permitir la contrucción del rtree. Esta función da inicio a la insercción de cada vector característico hacia el RTree.
- **uploadPicture**
Esta función es para permitir al usuario la consulta de las k imágenes mas cercanas. Recibo 2 parametros: la imagen en consulta y el valor de k. Esta función da inicio a las funciones de búsqueda secuencial y búsqueda en RTree. Finalmente retorna al usuario las imágenes más cercanas de acuerdo a los 3 criterios mencionados antes. 
- **main**
Esta función permitira hacer la llamada a **preprocess** y **load_var**.


### Pruebas
La vista se separa en 2 partes, una para la subida de la imagen e ingreso del valor k y otra para la muestra de resultados.

#### Input 1: Imagen de Abid Hamid
![Imagen1](/input/abidhamid.jpeg)

#### Output1: k=4
![Imagen1](/output/results1.png)

#### Input 2: Imagen de William Builger 
![Imagen1](/input/william-builger.jpg)

#### Output2: k=4
![Imagen1](/output/results2.png)


# Experimento 1
|Precision|ED|MD|
|---|---|---|
|k=4|1|1|
|k=8|1|0.875|
|k=16|0.815|0.75|

#### Input: Winona Ryders
![Imagen1](/img/winona.jpg)

#### k=4
![Imagen1](/img/k_4.png)

#### k=8
![Imagen1](/img/k_8.png)

#### k=16
![Imagen1](/img/k_16.png)

# Experimento 2

Resultados para cada valor de n. Seq/Eucl, es el desempeño para la la búsqueda por distancia euclideana y Seq/Manh es el desempeño para la búsqueda por distancia manhattan. En el experimento se trabaja con k=4.
![Imagen1](/img/times.png)

Gráfica de desempeños para cada valor de n.
![Imagen1](/img/graphic_t.png)