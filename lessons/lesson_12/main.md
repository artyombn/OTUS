# Основы HTTP взаимодействия
## (Hypertext Transfer Protocol) 

*Знакомство с HTTP:*  
*- HTTP методы и статус коды*  
*- apispec (swagger)*


*HTTP documentation:*
*https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods*


## HTTP методы
<span style="color: #00cccc;">GET</span> - метод запроса данных с сервера без необходимости их изменения
*(!!! Данные запросы должны получать только данные!)*

<span style="color: #00cccc;">HEAD</span> - для получения заголовков ответа без тела ответа. Полезно, чтобы узнать информацию о ресурсе, без получения его содержимого

<span style="color: #00cccc;">POST</span> - создание. Используется для отправки данных на сервер для обработки. Обычно POST запрос используется для создания новых ресурсов на сервере или изменения существующих.
*(имеет тело запроса)*

<span style="color: #00cccc;">PUT</span> - используется для полного обновления ресурса на сервере или создания нового ресурса. *(заменяет все значения ресурса. то есть нужно отправить все данные для обновления, даже если эти данные остаются неизменными)*

<span style="color: #00cccc;">PATCH</span> - используется для частичного обновления ресурса на сервере. В отличие от PUT запроса, который обновляет ресурс полностью, PATCH запрос обновляет только указанные атрибуты ресурса или его часть.

***Safe*** *- безопасные методы, не изменяют состояние сервера или ресурсов*  

***Idempotent*** *- идемпотентные методы, которые можно вызывать несколько раз, и результат будет таким же, как при однократном вызове.
Вызов одного и того же запроса повторно не приведет к изменениям.*

***GET:*** *Safe, Idempotent*  
***HEAD:*** *Safe, Idempotent*  
***POST:*** *No Safe, No Idempotent*  
***PUT:*** *No Safe, Idempotent*  
***PATCH:*** *No Safe, No Idempotent*    
***DELETE:*** *No Safe, Idempotent* 


## Status Codes:  
*https://developer.mozilla.org/en-US/docs/Web/HTTP/Status*  

<span style="color: #ff602b;">404</span> - страницы нет на сервере или для пользователя скрыт доступ

Informational responses <span style="color: #ffdb3b;">(100 – 199)</span>  
Successful responses <span style="color: #87ed68;">(200 – 299)</span>  
Redirection messages <span style="color: #75cdff;">(300 – 399)</span>  
Client error responses <span style="color: #ff602b;">(400 – 499)</span>  
Server error responses <span style="color: #ff602b;">(500 – 599)</span>  

## HTTP HEADERS
*https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers*

Это часть HTTP-запросов и ответов, которая содержит метаданные о передаваемых данных.  
***Пара Имя + Значение*** *(Имя заголовка + Его содержание)*  
Заголовки - служебная информация, с которой работают клиент и сервер

## SWAGGER- интерактивная документация по запросам
*https://petstore.swagger.io*  
*https://httpbin.org/#/*  
*https://httpie.io/app*
