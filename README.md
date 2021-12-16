
## Flask file upload sample

### Start 

```sh
$ mkdir -p files
$ python3 -m venv venv
$ venv/bin/pip install -r requirements.txt
$ venv/bin/gunicorn -b ':8000' --reload app:app
```

### Test

```sh
$ curl -XPOST -F 'file=@app.py' http://token:aaaa@localhost:8000/upload

$ ls -l files 
total 8
-rw-r--r--  1 byung-kyukim  staff  529 Dec 16 21:02 app.py
```