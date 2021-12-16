from flask import Flask, request
import base64
import json
 
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save('./files/' + f.filename)

    if 'Authorization' in request.headers:
        bauth = request.headers['Authorization']
        token = bauth.split(' ')[1]
        auth = base64.b64decode(token).decode('utf-8')
        print(auth)
    return {'result': 'ok'}
 
if __name__ == '__main__':
    app.run()

