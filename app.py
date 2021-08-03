from flask import Flask, json, request, jsonify
import os
from main import Calculator
import urllib.request
from werkzeug.utils import secure_filename
from checkers.constants import WHITE, RED
 
app = Flask(__name__)
 
app.secret_key = "caircocoders-ednalan"
 
UPLOAD_FOLDER = 'pics'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/')
def main():
    return 'Homepage'
 
@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'white' not in request.files and 'black' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
 
    to_move = None
    if 'white' in request.files:
        files = request.files.getlist('white')
        to_move = WHITE
    else:
        files = request.files.getlist('black')
        to_move = RED
     
    errors = {}
    success = False
     
    for file in files:      
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'
 
    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        calc = Calculator()
        resp = jsonify(calc.main(to_move))
        #resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        directory = './pics'
        for filename in sorted(os.listdir(directory)):
            os.remove(directory + '/' + filename)
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
 
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False)