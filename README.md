## REST API на DRF c использованием SqLite библиотеки.

### Сущности:
- **User (Dealer)**
- **Car**
- **Application**

### Пример запросов к API:

**/api/dealers/** - создание дилера, отображение списка дилеров

**/api/dealers/id** - отображение/удаление/изменение выбранного дилера

Доступ к урле с дилерами есть только у администратора.


В API есть аутентификация и авторизация, сделанная по принципу:

Машины видят все пользователи.

Создавать машины могут только зарегистрированные пользователи (дилеры).

### Регистрация по урле: 

**/api/auth/users/**

принимает **post** запрос

с полями в **json** формате, *пример*:

{
  'username' : Tom,   
  'email' : 'tom@gmail.com',   
  'password' : 'sdcscdcc7dc6s7dcybsudc'    
}

пример ответа:


{

   "email": "tom@gmail.com",  
   "username": "Tom",   
   "id": 1     
   
}

Редактировать/удалять машины могут только те пользователи (дилеры), которые создали соответствующие машины.



### Пример создания машины:

**/api/cars/** - создание машин дилером, отображение списка машин

{

        "dealer_name": "BMW",
        "model": "BMW X1",
        "engine": "140 л.с",
        "color": "Blue",
        "price": 4000000,
        "description": "В ожидании знаковых событий: новый BMW X1 появился, чтобы задавать новые стандарты. Его стремление действовать выражается прежде всего в спортивном дизайне."
  
}

**/api/cars/id** -  отображение/удаление/изменение выбранной машины


По урле **/api/application/** пользователь сайта может оставить заявку на выбранную им машину, 
после чего заявка будет сохранена в базу данных и соответствующему дилеру на почту прийдет сообщение 
с информацие о заявке.

### Пример создания заявки:
**/api/application/**   принимает **post** запрос
{

        "id": 1,
        "name": "Vasya",
        "email": "vasya@gmail.com",
        "number": "8952637455",
        "application_subject": "test",
        "car_id": 1
}

**/api/application/**   
принимает **get** запрос по которому каждому дилеру отображается список заявок, которые относятся к его машинм.


**/api/application/id**
принимает **get/delete/put** запросы по которым диелры могут изменять/удалять/смотреть свои заявки. 






