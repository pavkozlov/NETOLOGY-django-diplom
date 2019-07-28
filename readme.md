# Дипломный проект по курсу «Django: создание функциональных веб-приложений»

## Задача

Разработать сайт интернет-магазина. (Должна быть реализована клиентская часть сервиса и интерфейс администрирования.)

## Реализовано

* Главная страница со статьями о подборке товаров (статьи отсортированы по дате создания) и перечислением этих товаров. Товары привязываются к статье в панели администратора.
* Страница категории товара со списком товаров с пагинацией. Показано сколько всего страниц, есть возможность перейти на следующую, предыдущую, первую, последнюю. По умолчанию на странице 2 товара. Если товаров в категории нет, выводится предупреждение.
* Страница товара с подробным описанием, отзывами. Есть возможность добавить анонимный отзыв (без регистрации), указав имя, текст и колличество звёзд.
* Корзина со списком выбранных товаров, привязанных к пользователю. (Привязка идёт по имени пользователя, если пользователь авторизован. В таком случае при заходе в свой аккаунт с другого устройства, данные в корзине сохранятся. Если пользователь не авторизован, ему выдаётся уникальный идентификатор, и привязка идёт по нему. При открытии/закрытии браузера данные в корзине сохранятся. Но пропадут, если очистить хранилище кэша и cookies или зайти с другого устройства). При нажатии на кнопку "Заказать", корзина очищается и создаётся заказ (виден в панели администратора)
* Для входа используется авторизация по e-mail адресу и паролю, вместо стандартной связки логин + пароль.
* Меню содержит ссылку на главную страницу, ссылки на разделы (разделы могут иметь иерархию), ссылку на корзину, кнопку Войти/Выйти в зависимости от статуса авторизации. Категории добавляются в меню автоматически. Страница на которой сейчас находится пользователь выделена.

## Интерфейс администратора

* Редактирование категорий.
* Редактирование товаров.
* Редактирование статей на главной странице и привязывание к ним товаров, которые должны отображаться после нее.
* Просмотр списка заказов пользователей, отсортированных по дате создания, с указанием пользователя, наименованй товаров и количества товаров.


## Дополнительно

* Для одинакового отображения сайта на мобильных устройствах, планшетах, телевизорах, компьютерах использован фреймворк Bootstrap
* Все запросы к базе данных оптимизированы, включено кеширование. Сайт имеет высокую скорость загрузки страниц.
* Backend реализован на Django 2.2.3
* В качестве СУБД используется sqlite3
* Структура проекта: Главный каталог -> Папка с базой данных (database) ; Папка со статическими файлами (static) ; папка проекта (OnlineShop)

## Изображения

![](mygif.gif)

## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:
```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py migrate
```

* Команда для загрузки данных в БД
```bash
python manage.py dumpdata > dumpdata.json
```

* Команда для запуска приложения
```bash
python manage.py runserver
```
