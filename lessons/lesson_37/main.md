# NumPy

- одномерные и многомерные массивы ndarray
- свойства ndarray
- базовые операции с массивом
- итерирование по элементам массива
- изменение массива

`pip install numpy`  
`import numpy as np`  
```python
np.ones(3)
np.ones(3, dtype=int)
np.zeros(4)
np.random.random(4)
np.random.randint(1, 100, size=(3, 4))
np.linspace(0, 2, 9)
array.ndim # узнать количество измерений массива
array.shape # длина массива
array.size# количество элементов массива - произведение длин всех осей
array.dtype # тип элементов массива
array.min()
array.max()
array.mean() # среднее арифметическое
array.prod() # умножение всех элементов
```

Преобразование одномерного массива в 3х мерный
```python
ar3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
ar4 = ar3.reshape(4, 3)
```
