# OpenCV

- распознавание объектов на видео
- добавление графики поверх изображения с камеры

https://opencv.org

`pip install opencv-contrib-python`  

Читаем картинку
```python
import cv2 as cv

def main()
    image_filepath = "data/cat.jpg"
    img = cv.imread(image_filepath)
```

Делаем картинку серой:  
`img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)`  

Сохраняем картинку:  
`cv.imwrite("data/cat-gray.jpg", img_gray)`  

`CASCADE = "haarcascade_frontalface_default.xml"` используется файл xml библиотеки OpenCV  
lib/site-packages/cv2/data/haarcascade  - все файлы, на которые будет ориентироваться сравнение


Поиск faces: 
```python
    faces = face_finder.detectMultiScale3(
        img_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE,
        outputRejectLevels=True,
    )

    if faces is None or len(faces) == 0:
        print("No results found")
        return

    print(faces)
```  


