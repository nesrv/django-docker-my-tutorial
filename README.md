# My tutorial 0.1

## Contributing

### Installing dependencies

If you want to contribute to this project, first create a Python virtual environment
for this project, using a tool such as [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

###  For example for first install virtualenvwrapper
1) 
```sh
pip install virtualenvwrapper
```
2) 
```sh
export WORKON_HOME=~/Envs
```

3)
```sh
mkdir -p $WORKON_HOME
```
4) 
a) for MAC
```sh
source /usr/local/bin/virtualenvwrapper.sh
 ```
b) for Ubuntu
```sh
source ~/.local/bin/virtualenvwrapper.sh
 ```
5)
```sh
mkvirtualenv env1
```

###  For install virtualenviroment from virtualenvwrapper
1) 
```sh
ls $WORKON_HOME
```

2) virtualenviroment testvenv1 for example
```sh
workon testvenv1
```

Install Poetry, a Python dependency manager, using the following command:

```sh
pip install -U pip poetry
```

You can now use the following command to install the dependencies of this project:

```sh
poetry install
```

[//]: # (Activate virtual environment)

[//]: # ()
[//]: # (```sh)

[//]: # (source .venv/bin/activate)

[//]: # (```)

### Configuration

Create (or copy) the `.env` file
The .env file must contain `JWT_PRIVATE_KEY`


### Running the application

Simply type 
```sh
python3 manage.py runserver 0.0.0.0:8000
```

### A. For start with docker 
1) Build the docker image
```sh
docker build -t door-manager-image .
```
2) Create and run container
```sh
docker run -p 8000:8000 door-manager-image
```
3) The working application is available at:
```sh
http://0.0.0.0:8000
```

### B. For start with docker-compose 

```sh
docker-compose up -d
```

At that point, the local server is initiated and accessible at 
``sh
http://0.0.0.0:8000
``
### Stop and remove containers, networks, images, and volumes

```sh
docker-compose down
```

Stop docker-compose services

```sh
docker-compose stop
```