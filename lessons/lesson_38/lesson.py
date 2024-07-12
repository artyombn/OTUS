import pandas as pd

print(pd.__version__)

titanic_df = pd.read_csv("titanic.csv")
# print(titanic_df)

salaries_list = [
    167.6,
    254.8,
    435.7,
    321.3,
    123.9,
    496.8,
]
print(salaries_list)

salaries_series = pd.Series(salaries_list)
print(salaries_series)
print(type(salaries_series))

print(salaries_series.to_list())
print(salaries_series.to_numpy())

workers_names = [
    "Bob",
    "Alice",
    "Nick",
    "John",
    "Sam",
    "Clark",
]
print(workers_names)
pd.Series(workers_names, name="Workers")

salaries_connect_workers = pd.Series(
    salaries_list,
    index=workers_names,
    name="Salaries",
)
print(salaries_connect_workers)
print(salaries_connect_workers["Sam"])
print(salaries_connect_workers.iloc[3])  # если хотим взять по индексу изначальному
print(salaries_connect_workers["Nick":"Sam"])
print(salaries_connect_workers.mean())
print(salaries_connect_workers.max())
print(salaries_connect_workers.min())
print(salaries_connect_workers.median())

a = pd.Series([1, 2, 1, 2, 2, 3, 3, 4, 1, 2, 5, 6]).value_counts()
print(a)
b = pd.Series([1, 2, 1, 2, 2, 3, 3, 4, 1, 2, 5, 6]).value_counts(normalize=True)
print(b)

s = salaries_connect_workers.copy()
print(s.sort_values())
print("---")
print(s.sort_values(inplace=True))

print(s.describe())
print(s.to_json())


workers_salaries_data = [
    {
        "name": "Bob",
        "salary": 167.6,
        "age": 18,
    },
    {
        "name": "Alice",
        "salary": 235.8,
        "age": 25,
    },
    {
        "name": "Nick",
        "salary": 435.7,
        "age": 33,
    },
    {
        "name": "John",
        "salary": 321.3,
        "age": 27,
    },
    {
        "name": "Sam",
        "salary": 123.9,
        "age": 20,
    },
    {
        "name": "Clark",
        "salary": 496.8,
        "age": 55,
    },
]

print(workers_salaries_data)

salaries_df = pd.DataFrame(workers_salaries_data)
print(salaries_df)

print(salaries_df.index)
print(salaries_df["name"])
print(salaries_df["age"])
print(salaries_df.iloc[0])
print(f"----")
for idx, series in salaries_df.iterrows():
    print("idx:", idx)
    print("series:", series)


# Модификация dataframe (добавление/изменение данных словаря)

countries_info = {
    "country": ["Russia", "Belarus", "Ukraine", "Kazakhstan"],
    "population": [145.5, 9.3, 41.0, 19.1],
    "square": [17_075_200, 207_560, 603_628, 2_725_000],
}
countries_index = ["RU", "BY", "UA", "KZ"]

countries_df = pd.DataFrame(
    countries_info,
    index=countries_index,
)

countries_df.index.name = "code"

print(f"countries_df ---> ")
print(countries_df)

print(
    countries_df.population * 1_000_000 / countries_df.square
)  # плотность населения на 1 кв. км.

countries_df["density"] = countries_df.population * 1_000_000 / countries_df.square
print(countries_df)
countries_df["density"].apply(round)
countries_df["density_int"] = countries_df["density"].apply(round)
print(countries_df)

# new = countries_df.drop("density", axis=1)
new = countries_df.drop(columns=["density_int"])
print(new)

print(titanic_df.head(5))
print(titanic_df.tail(5))
print(titanic_df.info())
print(titanic_df.describe())
print(titanic_df.columns)


print(titanic_df.Age)
# print(titanic_df.Age.values)
print(titanic_df.Pclass.value_counts().sort_index())

print(titanic_df.Sex.value_counts())
print(titanic_df.value_counts("Sex"))

print(titanic_df.value_counts(["Sex", "Pclass"]))
print(titanic_df.value_counts(["Sex", "Pclass"]).to_frame())

print(
    titanic_df.pivot_table(
        values=["Age"],
        index=["Sex", "Survived"],
        columns=["Pclass"],
        aggfunc="median",
    )
)
