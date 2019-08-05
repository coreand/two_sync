## Setup
```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```
Use username: admin, password: admin for super user or change settings in `config.json` if you want custom user.

## Launch
Run this command in the directory `./store`: 

`python manage.py runserver 127.0.0.1:8001`

And run this command in the directory `./warehouse`: 

`python manage.py runserver 127.0.0.1:8002`
