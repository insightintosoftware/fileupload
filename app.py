from flask import render_template
from flask import Flask, request
import requests
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('file_upload_test_input.html', title='File Upload - Input')

@app.route('/drag_and_drop')
def drag_and_drop():
    return render_template('file_upload_test_drag_and_drop.html', title='File Upload - DragAndDrop')

@app.route('/textarea')
def textarea():
    return render_template('file_upload_test_textarea.html', title='File Upload - Textarea')

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'data' not in request.files:
            return 'error'
    file = request.files['data']
    file.save("./temp_files/"+request.form['chunk_id'])

    chunk_length = int(request.form['chunk_length'])
    chunk_split = request.form['chunk_id'].split('_');
    chunk_prefix = chunk_split[0]
    chunk_seq = int(chunk_split[1])
    if chunk_length == chunk_seq + 1:
        filenames = [filename for filename in os.listdir('./temp_files') if filename.startswith(chunk_prefix)]
        filenames = sorted(filenames)

        with open("./UploadedFiles/"+request.form['filename'], "ab") as myfile:
            for f in filenames:
                with open('./temp_files/' +f, "rb") as input_file:
                    myfile.write(input_file.read())
                os.remove('./temp_files/' +f)

    return 'success'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5070)