# Перечень статей для самообразования/заглянуть обновить данные

### Общее:

* [Куча, хэш, списки](https://habrahabr.ru/post/263765) 
* [оценка сложностей алгоритмов](https://habrahabr.ru/post/196226/)   
* [Алгоритмы и типы данных в популярных программах] https://habrahabr.ru/company/wunderfund/blog/277143/
* [Набор шпаргалок](http://habrahabr.ru/post/254585/)  
* [паттерны в метафорах](https://habrahabr.ru/post/136766/)  
* [спискота книг по мнению mail.ru](http://habrahabr.ru/company/mailru/blog/265103/) 
* [процесс перехода на сайт: от ввода теста, до получения ответа](http://habrahabr.ru/company/htmlacademy/blog/254825/) 


## БЭКЕНД PYTHON:

### Про Pyhon:

* yolk замена pip
* wheels замена eggs 
* pypy — добавь скорости
* greenlet vs async await

* [питон на хабре сборник ссылок](http://habrahabr.ru/post/205944/) 
* [грабли и уловки python](http://idzaaus.org/static/files/articles/Python_Tips,_Tricks,_and Hacks_(rus).pdf) 
* [как устроин GIL в python](https://habrahabr.ru/post/84629/)  
* [потоки просто](http://habrahabr.ru/post/260431/) 
* [приколы с eval](http://habrahabr.ru/post/260431/) 
* [wheels как замена eggs](http://habrahabr.ru/post/210450/) 
* [магические (__method__) методы](http://habrahabr.ru/post/186608/) 
* [путь для абсолютного импорта модуля в python2 импортим с __future__](http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path) 
* [pep8 автоформатирование](http://habrahabr.ru/post/251531/) 
* [питон алгоритмы, структура данных учебник](http://aliev.me/runestone/) 
* [профилирование python](http://habrahabr.ru/company/mailru/blog/201778/) 


### Заметки про python на android:

#### sl4a:
* https://xakep.ru/2011/08/18/56526/ -простенькая програмка
* http://habrahabr.ru/post/122188/ средняя программка
* http://www.ibm.com/developerworks/ru/library/mo-python-sl4a-1/

####kivy:
* https://habrahabr.ru/post/149898/  сделаное приложение для фотографий

#### альтернатива в виде pygame:
* http://games.renpy.org/ фреймворк для создания визуальных новел

### Старые заметки по celery:
* http://habrahabr.ru/post/123902/ Просто вкорячим асинхронные задачи
* http://habrahabr.ru/post/158961/ RabbitMQ с Celery и без

###Заметки по торнадо:
* https://habrahabr.ru/post/252575/ многопользовательский шутаган на asyncio
* https://habrahabr.ru/post/230607/ Хостинг картинок
* https://habrahabr.ru/post/270709/ Python 3.5 async await yield from и движок motor по mongodb

### Про Flask:
#### Фласк говно:
* http://asvetlov.blogspot.ru/2014/10/flask_20.html в кратце — херовые рутины, глобальные singletone в виде импортов
#### Фласк наше все:
* http://habrahabr.ru/post/234785/ учебник

### Про Django:
* https://habrahabr.ru/post/264269/ Мутим свой облачный сервис на linux docker django:

###Тестирование:
* http://habrahabr.ru/post/248559/ selenium
* http://habrahabr.ru/post/244009/ selenium + django webtest
* http://habrahabr.ru/post/141209/ mock objects 
* http://kmike.ru/django-functional-testing-ru/ функциональное тестирование джанги
* незабыть про factory-boy как замена фикстур
* http://www.slideshare.net/JetStyle/python-django-16824866

### Про магизины Магазин (e-commerce)
* в кратце все плохо, живой только oscar или мутить что-то на django-cms или велопиедить на django
* http://www.django-cms.org/en/
* http://oscarcommerce.com/

## DEVOPS:

* http://kurapov.name/rus/technology/unix/  Микро Шпаргалка по юниксам

### Ansible:
* http://habrahabr.ru/company/express42/blog/254959/ быстрый старт
* http://habrahabr.ru/company/selectel/blog/270209/ изменения в 2.0
* http://habrahabr.ru/company/infobox/blog/252461/ длинный ман

### Vagrant:
* http://eax.me/vagrant/ начало работы с вагрант

* фикс под vmware, чтобы видеть bios  http://www.howtogeek.com/howto/16876/how-to-increase-the-vmware-boot-screen-delay/ 

### docker
* http://eax.me/docker/ вводная, в краце легче виртуалок, но ебля с адресами()
* http://habrahabr.ru/post/253877/ понимая докер
* http://habrahabr.ru/post/234829/ оптимизация образов (быть внимательным с весом образов при удалить добавить файлы)
* http://habrahabr.ru/post/261415/ свой облачный сервис на ansible и docker swarm(удобно мониторить и управлять контейнерами)

### nginx:
#### разные варианты деплоя (устаревшее )
* http://habrahabr.ru/post/264219/ Ip база делаем
* http://www.vivazzi.ru/blog/18/
* http://habrahabr.ru/post/226419/ uwsgi
* http://habrahabr.ru/post/159575/ привычный вариант с gunicorn
* http://habrahabr.ru/post/256481/ fastcgi + web2.py
* http://habrahabr.ru/post/272381/ готовые конфиги

### SQL:
* http://habrahabr.ru/company/mailru/blog/266811/ как работает реляционная база данных
* http://habrahabr.ru/post/272373/ tsql для игры в судоку
* http://habrahabr.ru/post/64851/ обзор движков mysql 
* http://habrahabr.ru/post/263541/ Postgresql приемы на продакшене
* https://habrahabr.ru/post/268949/ в защиту mysql

### NOSQL:
* redis:
* https://habrahabr.ru/post/271487/ под капотом redis
* http://habrahabr.ru/post/204354/ шпаргалка по redis

## ФРОНТ:
* https://habrahabr.ru/post/277323/ плачь  на тему количества современных фреймоврков на js


### производительность:
* http://habrahabr.ru/post/264639/  about:tracking мониторим производительность в chorme
* http://habrahabr.ru/company/paysto/blog/254619/ основные ловушки при использование кэша в html5 приложениях
* http://habrahabr.ru/post/137318/ оптимизация js

### javasrcipt:
* https://habrahabr.ru/post/231071/ вопросы для собеседований
* https://habrahabr.ru/post/253033/ более свежие
* http://learn.javascript.ru/ учебник онлайн
* http://habrahabr.ru/company/plarium/blog/270353/ es6
* http://shamansir.github.io/JavaScript-Garden/ грабли при использовании javascript
* http://habrahabr.ru/post/246349/ yeoman как сборщик
* http://habrahabr.ru/post/120192/  фишки под Js (устаревшее)
* http://habrahabr.ru/post/52201/ jquery наше все
* http://habrahabr.ru/post/175283/ 24 совета, на некосячить
* http://habrahabr.ru/post/249525/ ошибки в js 
* http://myway-blog.ru/javascript-data-storage/ хранения данных на фронте session localstorage

### html и css:
* https://habrahabr.ru/post/244929/ вопросы на собеседование
* http://htmlacademy.ru/blog/14 полезные рассылки
* http://frontender.info/wtfhtmlcss/ грабли при использовании html и css
* http://habrahabr.ru/post/263169/ css 12 мелких фишек
* http://habrahabr.ru/post/262783/ css 12 мелких фишек
* http://habrahabr.ru/post/263061/  так верстают не мудаки 
* http://codehipsters.com/2014/11/27/sitnik-interview.html postcss давит less и sass

### angular 1
* https://github.com/jmcunningham/AngularJS-Learning/blob/master/RU-RU.md хор ссылки 
* https://xakep.ru/2013/10/25/anglurjs/ плюсы ангуляра
* http://habrahabr.ru/post/246905/ минусы ангуляра
* http://habrahabr.ru/post/247283/ краткий учебник
* http://habrahabr.ru/post/244925/ перевод курсов
* https://makeomatic.ru/blog/2013/08/17/AngularJSAdvanced/ директивы и провайдеры
* http://devacademy.ru/posts/rukovodstvo-po-stilyu-programmirovaniya-i-oformleniya-prilozhenij-na-angularjs/ паттерны поведения
* https://habrahabr.ru/post/230761/ не стреляем по ногам 
* http://habrahabr.ru/company/infopulse/blog/262389/   ускоряем ангуляр 
* http://habrahabr.ru/post/269827/    ускоряем ангуляр 

###nodejs
* http://habrahabr.ru/company/mailru/blog/255895/ ошибки в разработке на ноде

## Вопросы по собеседованиям:

Итак, перед тем как пойти на собеседование ответь про себя на следующие вопросы:
Хочешь ли ты почитать такие книги:
Расширяем книжную полку: «Приемы объектно-ориентированного проектирования. Паттерны проектирования», «Рефакторинг. Улучшение существующего кода», «Чистый код: создание, анализ и рефакторинг», «Программист-прагматик. Путь от подмастерья к мастеру» однозначно стоят потраченного времени и денежных средств. Техники, описанные в этих книгах, универсальны для всех ЯП и пригодятся каждому программисту. 

Знаешь лы ты ответы на вопросы:

### 1. Python
- Какие бывают типы данных в Python?
- Чем отличается list от tuple?
- Что такое immutable объекты? Какие Вы знаете? В чем особенность?
- Что такое dict? Что может являться ключом? Что не может являться ключом? Каким образом нужно изменить класс что бы он смог быть ключом?
- Что такое декораторы? ( http://habrahabr.ru/post/141411/ )
- В какой момент вызывается декоратор?
- Может ли декоратор НЕ возвращать декорируемую им функцию?
- Можно ли декорировать класс?
- Может ли класс быть декоратором
- Что такое новые классы? чем отличаются от старых классов? ( http://habrahabr.ru/post/114576 / )
- Чем отличается @staticmethod от @classmethod? 
- Что происходит при обращении к property b экземпляра класса А? Как ищутся properties/methods класса? ( http://habrahabr.ru/post/114585/ )
- Что происходит если property не найдено?
- Что такое MRO? алгоритм решения проблемы?
- Что такое metaclass? ( http://habrahabr.ru/post/114585/ )
- Как создать metaclass?
- Как сделать класс использующий metaclass?
- Что такое процессы и потоки в Python? Какие возникают проблемы?
- Какие есть решения для синхронизации данных при работе с потоками?
- Что такое GIL?
- Что такое итераторы?
- Что такое генераторы?
- Что такое list comprehensions?
- Что быстрее встроенные функции map reduce filter или аналогичный код просто через for? Почему?
- Что значит ключевое слово global?
- Какие особенности областей видимости в Python?
- Зачем нужен код исключения?
- Что такое lambda?

### 2. Django
- Какой основной шаблон проектирования лежит в основе фреймверка?
- Что пошагово происходит когда пользователь нажал на ссылку? от браузера до приложения и обратно.
- Что такое middleware?
- Как сделать сообщение с трейсбеком при ошибке(500.html недостаточно)?
- Какие типы отношений между таблицами бывают в Django-ORM?
- Как реализовать отношение ManyToMany без ORM?
- Какие встроенные сигналы бывают в Django?
- Основные способы развертывания приложений?
- Что такое mod_wsgi?
- Что такое fixtures?

### 3. SQL
- Что такое внешний ключ и зачем он нужен?
- Что такое GROUP BY?
- Что такое ORDER BY?
- Что обозначает ключевое слово HAVING?
- Что в чем отличие между LEFT JOIN, RIGHT JOIN и INNER JOIN?
- Что такое хранимая процедура
- Чем отличается функция от процедуры

### 4. Unix
- Можно ли сделать ssh подключение к другому компьютеру с компа, к которому ты итак уже подключен через ssh? как это сделать?
- Права к файлам
- Нагрузка

### 5. SCM
- Можно ли удалить коммиты из репозитория в git? Как?
- Можно ли восстановить коммиты?
- В чем отличие веток git от веток в svn?
- Что такое git reset?
- Что такое git rebase?
- Чем git rebase отличается от git merge?

### 6. Алгоритмы
- Что такое сложность алгоритмов? Как вычисляется?
* Какова сложность алгоритма 
```for i in x:
    for j in y:
        i*j```
- Какие алгоритмы сортировки знаете?
- Какие есть способы обхода дерева?

### 7. Прочее
- Что такое doctype в html?
- Что такое meta в html?
- Что значит переменная g в Flask?

### Дополнительно:
#### Go
* http://golang-book.ru/ учебник на GO

#### Проектирование, потоки?
Ответь что такое гринлеты, Twisted, Tornado, в чём отличие мультипроцессинга от потоков, в чём их отличия в модулях Python(тест пройден если человек скажет что GIL работает в обоих случаях, а сами модули имеют одинаковый набор функций).
Про проектирование достаточно сложно говорить. Попроси придумать простейший Singleton и объяснить какие альтернативы этому решению есть. Скажет что-то про мета-классы, про то, что сами по себе модули являются синглтоном — тест пройден.
Спроси что такое кольцевые зависимости. Дай пример кода с такой проблемой и попроси решить её или аргументировать почему выхода нет. Тест пройден если человек переместит все run-time используемые импорты в конец файла или перепроектирует систему, предложив вариант без кольцевых зависимостей.
