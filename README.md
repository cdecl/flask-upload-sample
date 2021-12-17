
## Flask file upload sample

### Start 

```sh
$ mkdir -p files
$ python3 -m venv venv
$ venv/bin/pip install -r requirements.txt
$ venv/bin/gunicorn -b ':8000' --reload app:app
```

### Test

##### octet-stream

```sh
$ curl -XPOST --data-binary "@$HOME/.ssh/id_rsa" -H "Content-Type:application/octet-stream" http://localhost:8000/upload

$ tree keys
keys
└── 127.0.0.1.key
```

##### form-data

```sh
$ curl -XPOST -F "file=@HOME/.ssh/id_rsa" http://localhost:8000/upload

$ tree files
files
└── 127.0.0.1
    └── id_rsa
```