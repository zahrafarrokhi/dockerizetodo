# commands for postgres

```bash
sudo apt install postgresql

sudo passwd postgres

su - postgres

psql
```
```sql
alter role postgres password '123';
```

```bash
sudo vi /etc/postgresql/12/main/pg_hba.conf
```
change:
local   all             postgres                                peer

to:
local   all             postgres                                md5

```bash
sudo systemctl reload postgresql
```


### create db in postgres

```bash
su - postgres

psql
```
```sql
create database todo_db;
```

-------------------------------

# Building docker image
First run 
```bash
docker build -f base/Dockerfile -t todo:latest . # because docker file assumes we're in main folder, not project
docker-compose up # or just docker-compose build
```

in base/Dockerfile we have
```dockerfile
FROM python:3.8-alpine

WORKDIR /home/app

COPY  project/requirements.txt .
...
```
This means that we're in the main folder not the project folder. So we have to build the image in the main folder.

## Volume vs COPY . .
You can either have `COPY . .` in your docker file, or link the project directory in docker-compose via a volume:

```yml
services: 
    django:
        build: .
        command: 
            /bin/ash -c 'python3 manage.py migrate &&
            gunicorn todo.wsgi:application --bind 0.0.0.0:8000'
        volumes: 
            - ./project:/home/app/
```
This is not a good practice in production environment.


