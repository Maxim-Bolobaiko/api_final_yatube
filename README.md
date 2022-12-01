# API для Yatube

API_Yatube - api для социальной сети YaTube на базе REST Framework. 
## Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Maxim-Bolobaiko/api_final_yatube.git
```

```
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```