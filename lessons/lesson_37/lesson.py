import numpy as np

array1 = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)

print(array1)

array2 = np.ones(3)  # [1. 1. 1.] - массив с плавающей точкой
array3 = np.ones(3, dtype=int)
print(array2)
print(array3)
array4 = np.zeros(4)
print(array4)
array4 = np.zeros([3, 4])
print(f"np.zeros(array) --> {np.zeros([3, 4])}")

# массив случайных чисел
array5 = np.random.random(4)
array6 = np.random.randint(1, 100, size=(3, 4))
print(array5)
print(f"array6 --> {array6}")
array7 = np.arange(10, 30, 5)
print(f"array7 --> {array7}")
array8 = np.linspace(0, 2, 9)
print(array8)

print(array6.ndim)
print(array6.shape)
print(array2.shape)
print(array2.shape)

print(array6.size)

print(array7.dtype)
print(array4.dtype)

a1 = np.array([1, 2, 3])
print(f"a1 --> {a1}")
a2 = np.array([10, 20, 30])
print(f"a2 --> {a2}")

a3 = a1 + a2
print(a3)
a4 = a1 - a2
print(a4)
a5 = a1 * 5
print(a5)

print(a2[1])
print(a2.min())
print(a2.mean())
print(a2.prod())


newarray1 = np.array(
    [
        [11, 2, 34, 0],
        [14, 5, 76, 10],
        [71, 18, 9, 21],
    ]
)
print(f"newarray1 --> {newarray1}")

newarray2 = np.array(
    [
        [1, 12, 42, 10],
        [4, 51, 62, 83],
        [94, 14, 6, 19],
    ]
)
print(f"newarray2 --> {newarray2}")

print(newarray2[1][1])
print(newarray2[1, 1])  # тоже самое, что и выше
print(newarray2[1][:3])
print(newarray2[1:3, :2])

ar3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"ar3 --> {ar3}, shape --> {ar3.shape}")

ar4 = ar3.reshape(4, 3)
print(f"ar4 --> {ar4}, shape --> {ar4.shape}")
