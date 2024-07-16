# API_final_yatube
## Описание:
Проект API Final Yatube, сделанный в рамках обучения на платформу Yandex.Practicum.
Проект представляет собой API, написанный с помощью Django Rest Framework. В его функционал входят:
1) аутентификация по токену (JWT + Djoser);
2) создание и получение постов (пост представляет собой текстовую публикацию от аутентифицированного пользователя);
3) создание и получение комментариев к постам;
4) просмотр групп;
5) также пользователя могут фолловить друг друга и просматривать список фолловеров (только для аутентифицированных пользователей).

## Как запустить проект на локальной машине:
Клонировать репозиторий и перейти в него:
```
git clone https://github.com/AndreiAgeev/api_final_yatube.git
```
```
cd api_final_yatube/yatube_api/
```
Создать и активировать вирутальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate # для Linux
source env/Scripts/activate # для Windows
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции и запустить проект:
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```

## Примеры
Полная документация по API доступна по ссылке http://127.0.0.1:8000/redoc/ после запуска проекта.

Отдельные примеры запросов к API:
1) Получение конкретной публикации
```
GET http://127.0.0.1:8000/api/v1/posts/{id}/
```
API возвращает JSON-объект, содержащий данные запрошенного поста:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
* "id" - id поста, **int**;
* "author" - автор поста, **string**;
* "text" - текст поста, **string**;
* "pub_date" - дата публикации поста, **string**;
* "image" - изображение, **binary string or null**;
* "group" - id группы, к которой может принадлежать пост, **int or null**

2) Получение списка фолловеров:
```
GET http://127.0.0.1:8000/api/v1/follow/
```
API возвращает список JSON-объектов с подписками пользователя, сделавшего запрос:
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```
* "user" - username владельца токена, **string**;
* "following" - username пользователя, на которого подписан владелец токена, **string**
