from flask import Flask, request
import datetime
import base64
import os
import logging

logging.basicConfig(
    format = '[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
 
app = Flask(__name__)

@app.route('/')
def index():
    return {'alive': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

def remote_addr():
    remote_addr = ''
    if 'X-Forwarded-For' in request.headers:
        remote_addr = request.headers['X-Forwarded-For']
    else:
        remote_addr = request.remote_addr
    return remote_addr

def get_basicauth():
    if 'Authorization' in request.headers:
        bauth = request.headers['Authorization']
        token = bauth.split(' ')[1]
        auth = base64.b64decode(token).decode('utf-8')
        return auth

@app.route('/upload', methods=['POST'])
def upload():
    content_type = request.headers['Content-Type']
    logging.info(content_type)
    
    addr = remote_addr()
    logging.info(addr)
    
    if 'application/octet-stream' in content_type:
        filename = './keys/{}.key'.format(addr)
        with open(filename, 'wb') as f:
            f.write(request.data)
    elif 'multipart/form-data' in content_type:
        f = request.files['file']
        path = './files/{}'.format(addr)
        os.makedirs(path, exist_ok=True)
        f.save('{}/{}'.format(path, f.filename))

    return {'result': 'ok', 'content-type': content_type}
 
if __name__ == '__main__':
    app.run()

