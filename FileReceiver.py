##imports##
from flask import Flask, request
import os

##code (I have no clue what to call this)##
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return  'No selected file', 400
    file.save(os.path.join('uploads', file.filename))
    return 'File uploaded successfully', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)