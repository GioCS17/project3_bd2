from flask import Flask
from flask import render_template 
from flask import request
from flask import jsonify
import json
from flask_cors import CORS
from ProcessRecognition import *
from PreProcess import *
from werkzeug.utils import secure_filename


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
        imagelist=[]
        for i in ans:
            imagelist.append(path_files[i][1:])
            print(path_files[i])

    return render_template("index.html",imagelist=imagelist)
    #return jsonify({'status': 201})

def main():
    preprocess(root)
    load_var()
if __name__=="__main__":
    main()
    app.run(debug=True)