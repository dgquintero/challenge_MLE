# Software Engineer (ML & LLMs) Challenge


## Build the Docker Image

```
docker build -t myimage .
```

## Start the Docker Container

```
docker run -d --name mycontainer -p 80:80 myimage

```

Interactive API docs
http://127.0.0.1/docs


## with out docker

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
pip3 install -r requirements-dev.txt
```

```
python3 challenge/api
```


