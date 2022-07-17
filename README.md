# API для соцсети Yatube

Позволяет взаимодействовать с блогом Yatube при помощи REST API. Весь функционал доступен. 
Документация к API доступна по адресу http://127.0.0.1:8000/redoc/.

## Инструкции по установке
Клонируйте репозиторий:
```git clone git@github.com:DostovaK/api_final_yatube.git```

Установите и активируйте виртуальное окружение:
- для MacOS
```python3 -m venv venv```
```source venv/bin/activate```
- для Windows
```python -m venv venv```
```source venv/Scripts/activate```

Установите зависимости из файла requirements.txt:
```python -m pip install --upgrade pip```
```pip install -r requirements.txt```

Примените миграции:
```python manage.py migrate```

В папке с файлом manage.py выполните команду:
```python manage.py runserver```

## Примеры
> GET Получение публикаций api/v1/posts/
```200:```

```sh
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

> POST Создание публикации api/v1/posts/
```200:```

```sh
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

> PATCH Частичное обновление публикации api/v1/posts/{id}/
```200:```

```sh
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

```401:```

```sh
{
  "detail": "Учетные данные не были предоставлены."
}
```

```403:```

```sh
{
  "detail": "У вас недостаточно прав для выполнения данного действия."
}
```

```404:```

```sh
{
  "detail": "Страница не найдена."
}
```

## License
BSD 3