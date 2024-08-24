# Django проект работы со "научным блогом"

Ключевые слова:
- django
- skypro_python41.0
- blog
- scientific
- astronomy

### Эволюция проекта
- [x] Созданы директории и локальное окружение
- [x] Создана база данных в posgress
- [x] Сделаны настройки для github 
- [x] Создан проект django и приложение newblog
  - комментарий: 
- [x] 


### создаем директории и локальное окружение

```bash
 export PY_PROJECT=scientific_news_blog #наименование проекта
 mkdir $PY_PROJECT  #создаем директорию проекта
 cd $PY_PROJECT #переходим в рабочую директорию
 python3 -m venv env #создаем виртуальное окружение
 source env/bin/activate #переходим в виртуальное окружение
 pip3 install --upgrade pip
 pip3 freeze > requirements.txt #записываем зависимости
 pip3 install -r requirements.txt
 touch .gitignore
 touch README.md
```


### настройка базы данных postgres 

```bash
[postgres@mycomputer ~]$ psql
Password for user postgres: 

postgres=# CREATE DATABASE news_blog_db  OWNER azamat;
CREATE DATABASE

[postgres@mycomputer ~]$ psql --username=azamat --host=127.0.0.1 --dbname=news_blog_db --password
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'news_blog_db', # Название БД
        'USER': 'azamat', # Пользователь для подключения
        'PASSWORD': 'crjhjcnm', # Пароль для этого пользователя
        'HOST': '127.0.0.1', # Адрес, на котором развернут сервер БД
        'PORT': 5432, # Порт, на котором работает сервер БД
    }
}
```

### github

create repository on github and synchronize with offline repository

```bash
git remote add origin git@github.com:vazastro78/scientific_vlog.git
git branch -M main
git push -u origin main


git checkout -b basic_settings #создаем и переключаемся на новую ветку
git checkout main

git checkout -b django
#git remote remove origin #удаляем связь с удаленным репозиторием
#git clone git@github.com:vazastro78/scientific_vlog.git
```

### создаем проект django и приложения mainapp, newsblog в нем

```bash
django-admin startproject config . #инициализируем проект
pip3 install -r requirements.txt 

python3 manage.py startapp mainapp
touch mainapp/urls.py
mkdir -p mainapp/templates/mainapp

python3 manage.py startapp newsblog
touch newsblog/urls.py
mkdir -p newsblog/templates/newsblog
mkdir -p static/css static/js static/imagesmkdir -p media/

```
