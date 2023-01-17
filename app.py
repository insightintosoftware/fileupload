from flask import render_template
from flask import Flask, request
import boto3
from boto3.s3.transfer import TransferConfig
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

@app.route('/paste')
def paste():
    return render_template('file_upload_test_paste.html', title='File Upload - Paste')

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

        file_path = "./UploadedFiles/" + request.form['filename']
        with open(file_path, "ab") as myfile:
            for f in filenames:
                with open('./temp_files/' +f, "rb") as input_file:
                    myfile.write(input_file.read())
                os.remove('./temp_files/' +f)

            """
            # If you want to do multipart upload it AWS S3, uncomment this part.
            # Actually, you don't need to explicitly ask for a multipart upload.
            # Just call upload_file, and boto3 will automatically use a multipart upload 
            # if your file size is above a certain threshold (which defaults to 8MB).
            bucket_name = 'xxx'
            access_key_id = 'xxx'
            access_secret = 'xxx'

            awssession = boto3.Session(aws_access_key_id=access_key_id, aws_secret_access_key=access_secret)
            s3 = awssession.resource('s3')
            config = TransferConfig(multipart_threshold=1024*25,
                                    max_concurrency=10,
                                    multipart_chunksize=1024*25,
                                    use_threads=True)
            
            key = "other/"+request.form['filename']
            s3.Object(bucket_name, key).upload_file(file_path,
                                                    ExtraArgs = {'ContentType': 'text/plain'},
                                                    Config = config)
            """

    return 'success'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5070)