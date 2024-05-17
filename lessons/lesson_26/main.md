# Основы Фронтенда

## HTML, CSS, JS

WEB tutorial:  
_https://www.w3schools.com/_

Пример оформления стилей в CSS:
```css
body {
    background: lightgreen;
    font-family: 'Bradley Hand', 'Arial Black', serif;
    font-size: 20px;
}
```

Подключение CSS стиля:
```css
<link
        rel="stylesheet"
        href="{{ url_for('static', filename='css/main.css') }}"
>
```

Классы в HTML
```html
<a
        class="green-link link-no-underline"
        href="{{ url_for('products_app.add') }}">
    Add a new product</a>
```
И обработка их в CSS:
```css
.green-text {
    color: green;
}

.link-no-underline {
    text-decoration: none;
}
```

Переопределение стиля в CSS:
```css
h1.green-text {
    color: #2659dc;
}
```