# Pandas

- индексы
- срезы
- Series
- DataFrame
- загрузка данных из файла
- группировка

`pip install pandas`  
`import pandas as pd`


https://pandas.pydata.org/docs/getting_started/index.html#intro-to-pandas  

`salaries_series = pd.Series(salaries_list)`  
Series - обертка Numpy

Выгрузить данные в list, numpy, json, csv
`salaries_series.to_list()`  
`salaries_series.to_numpy()` 
`salaries_series.to_json()`  
(есть множество и других методов записи/отображения данных по форматам)  

Загрузить данные с файла (например csv):  
`salaries_series.rad_csv('folder/file.csv', sep=',')`   
sep - разделитель  
index-col - указать какая колонка будет индексом  


с указанием названия series:  
`pd.Series(workers_names, name="Workers")`  

Связать 2 таблицы, назначив indexом одну из них  
```python
salaries_connect_workers = pd.Series(
    salaries_list,
    index=workers_names,
    name="Salaries",
)
```
```python
salaries_connect_workers.mean()
salaries_connect_workers.max()
salaries_connect_workers.min()
salaries_connect_workers.median()
```
Получить количество повторяющихся значений в Series  
`pd.Series([]).value_counts()`  
`pd.Series([]).value_counts(normalize=True)` - % повторений  

Сортировка значений
`s.sort_values()` - по возрастанию
`s.sort_values(inplace=True)` - по убыванию  

`s.describe()` описание series  
`s.info()` служебная инфа series  
`s.columns` посмотреть список всех колонок  

Пример вывода:
```python
None
count      6.000000
mean     300.016667
std      147.093459
min      123.900000
25%      189.400000
50%      288.050000
75%      407.100000
max      496.800000
Name: Salaries, dtype: float64
```

После получения данных в виде Json, мы можем сгенерировать в PD через метод DataFrame:  
`salaries_df = pd.DataFrame(json_file)`  

Для отображения информации о индексе:  
`salaries_df.index`  


Итерирование по данным:  
```python
for idx, series in salaries_df.iterrows():
    print("idx:", idx)
    print("series:", series)
```

Модификация dataframe (добавление/изменение данных словаря)  
`countries_df["density"] = countries_df.population * 1_000_000 / countries_df.square` - добавление колонки  
`new = countries_df.drop(columns=['density'])` - удалить колонку (не удаляет в текущем словаре, а создает новый)  

Работа с файлом titanic.csv  
`print(titanic_df.head(5))` - вывести первых 5  
`print(titanic_df.tail(5))` - вывести последних 5  

Сводные таблички:  
```python
    titanic_df.pivot_table(
        values=["Age"],
        index=["Sex", "Survived"],
        columns=["Pclass"],
        aggfunc="median",
    )
```