# Хранение данных в реляционных БД
## SQL, Postgres


_**SQLite**_ _- СУБД, где вся база данных хранится в 1 файле
(обычно для простых проектов)_

https://sql-academy.org/ru

- postgres docker  
- sql docker  
- mariadb docker  

### Postgres docker
https://hub.docker.com/_/postgres

_**Docker Compose** - файл, в котором находится структура запуска Docker приложений
(включая контейнеры, зависимости, настройки и др. параметры)  
Файл YML_

`docker compose up -d` - запустить все, что есть в файле конфигурации .yml  
`docker compose up -d pg` - запустить только postgres  
`docker compose ps` - отображение состояния контейнеров  
`docker compose stop` - завершить compose, без потери данных  


## SQL code

`VARCHAR(100)` - позволяет хранить строки различной длины, от одного символа до максимального значения = 100. можно не указывать (100)  
`SERIAL` - тип данных автоматически увеличивает значение при каждой новой записи  
`PRIMARY KEY` - определяет столбец или группу столбцов, которые уникально идентифицируют каждую запись в таблице  
`TEXT` - для больших текстов  
`DEFAULT ''` - указываем значение DEFAULT которое будет равно ''   
`NOT NULL` - проверка что поле не NULL  

**_Создание таблицы_**  
```
CREATE TABLE <table_name>
(
    <column_1> FEATURES,
    <column_2> FEATURES,
    ...
);
```
**_Поиск по таблице_**
```
SELECT * 
FROM <table>
ORDER BY <column> DESC;
```

`*` - все элементы таблицы (можно выбрать определенное поле  `SELECT id, username`)   
`ORDER BY id;` - отсортировать по id (`DESC` - обратный порядок)  

_**Заполнить ячейку таблицы значениями:**_  
```
INSERT INTO <table>(<column1>, <column2>, ...)
VALUES ('value1', 'value2'),
       ('value3', 'value4');
```

**_Добавить столбец в существующую таблицу_**
```
ALTER TABLE <table>
ADD COLUMN <column_name> VARCHAR UNIQUE;
```

**_Обновление значения ячейки_**  
```
UPDATE <table>
SET <column_name> = 'new_value'
WHERE <column_name> = 'key';
```

**_Полезные функции:_**  
`length(column_name)` - вывести длину значения  
`concat(column_name, 'value')` - склеить все значения в колонке с `'value'`  
`count(<table>.<column>) "new_column_name"` - посчитать кол-во совпадений  

_**Фильтрация:**_  
```
WHERE <column_name> ilike '%rambler.%'
ORDER BY id;
```
`ilke` - найди похожее, `%` - опускает то, что находится ДО или ПОСЛЕ поискового значения (в зависимости где стоит)  


**_Создать связь одной таблицы с другой_**  
_Например, связь по id_
```
CREATE TABLE <table_1>
(
    <column_1> SERIAL PRIMARY KEY,
    <column_2> VARCHAR(100) NOT NULL,
    <column_3> TEXT NOT NULL DEFAULT '',
    <column_for_binding> INTEGER NOT NULL,

    CONSTRAINT fk_autors
        FOREIGN KEY (<column_for_binding>)
            REFERENCES <table_2>(<column по которому связывать>)
);
```
`CONSTRAINT <name_bindings>` - для связи таблиц по ключу `<column_for_binding>`  
_*Показывает ограничение, то есть `<column_for_binding>` должно обязательно принадлежать `<table_2>(<column>)`  
Если не находит значение во второй таблице - не создает значение в первой_

`fk_autor` - fk_ + table_name которую хотим связать  
  

**_Показать значения первой таблицы, объединив с определенными колонками второй_**  
```
SELECT *
FROM <table_1> t1
JOIN <table_2> t2 ON t1.<column1> = t2.<column2>;
```
_Пример:_
```
SELECT *
FROM posts p
JOIN autors a ON a.id = p.autor_id;
```

_GROUP BY & count()_
```
SELECT a.id, a.username, count(p.id) "posts-count"
FROM autors a
JOIN posts p ON a.id = p.autor_id
GROUP BY a.id;
```

