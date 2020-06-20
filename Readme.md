# REST API (Python/Flask), JSON хранилище.
____

## Для работы с API требуется установка фреймворка Flask:

```pip-install flask```

### Команды для получения информации о пользователях:

```curl -i http://localhost:5000/users - вывести список пользователей
curl -i http://localhost:5000/users/user_id - поиск пользователя по id```

### Команды для добавления и обновления информации о пользователях:

#### Linux

```curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Имя пользователя"}' http://localhost:5000/users - добавление пользователя
curl -i -H "Content-Type: application/json" -X PUT -d '{"name":"Измененное имя"}' http://localhost:5000/users - изменение пользователя```


#### Windows

```curl -i -H "Content-Type: application/json" -X POST -d "{"""name""":"""Имя пользователя"""}" http://localhost:5000/users
curl -i -H "Content-Type: application/json" -X PUT -d "{"""name""":"""Измененное имя"""}" http://localhost:5000/users```

### Команда удаления информации о пользователях:

```curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/users/user_id```