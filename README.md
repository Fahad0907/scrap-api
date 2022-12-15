# scrap-api
###First you have to clone the git repo.
###Then create a virtual environment by..
```
python -m venv venv
```
###Then activate the environment by using this command
```
venv\Scripts\activate
```
###Install the libraries by using..
```
pip install -r requirements.txt
```
###Then you have to migrate the project
```
py manage.py migrate
```
###Run the server using.
```
py manage.py runserver
```

##Now for seeing the output you have to put a POST request using 'http://127.0.0.1:8000/scrap/output/' . in the request body , you have
to provide keyword in json format like 
```
{
    "keyword": "vim"
}
```

