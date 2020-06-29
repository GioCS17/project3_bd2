from flask import Flask
from flask import render_template 
from flask import request
from flask import jsonify
import json
from flask_cors import CORS
from ProcessRecognition import *
from PreProcess import *
from werkzeug.utils import secure_filename
import base64


# instantiate the app
app = Flask(__name__)
# Path of files
root= './lfw/'
path_photos='./photos/'

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@app.route("/")
def index():
    return render_template("index.html")

# Cortesia del profesor Heider 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/buildRtree")
def buildRtree():
    build_Rtree()
    return jsonify({'status': 201})

@app.route("/upload",methods=['POST'])
def uploadPicture():
    print("Computing Photo ...")
    k=request.form['text']
    file=request.files['file']
    print("Name of file::",file.filename)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(path_photos,filename))
        ans=knn(path_photos+file.filename,int(k))
        print(ans)
        data=[]
        ind=0
        for i in ans:
            file_ans = open(path_files[i][:-1],"rb")
            data.append(base64.encodebytes(file_ans.read()).decode('utf-8'))
            ind+=1

    return jsonify({'status': 201,'data_images':data})

def main(n):
    preprocess(root,n)
    load_var()

if __name__=="__main__":
    n=12800
    main(n)
    app.run(debug=True)