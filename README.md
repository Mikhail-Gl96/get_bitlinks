Скрипт для сокращения ссылок 
======

Скрипт для сокращения ссылок с помощью сервиса https://bitly.com<br>
Если вы уже сокращали введенную ссылку, вы получите информацию о количестве кликов по вашей сокращенной ссылке

#### Бот работает с версиями Python 3.6+ <br>С версиями ниже бот не работает!!!

## Настройка для использования на личном ПК
1. Скачайте проект с гитхаба
2. Перейдите в папку с ботом с помощью консоли и команды `cd <путь до проекта get_bitlinks>`<br>
3. Установить зависимости из файла `requirements.txt`<br>
   Библиотеки к установке: `requests`, `python-dotenv`<br>
   
   Возможные команды для установки:<br>
   `pip3 install -r requirements.txt`<br>
   `python -m pip install -r requirements.txt`<br>
   `python3.6 -m pip install -r requirements.txt`
4. Создайте файл .env
5. Запишите в файл .env переменные:
    `BITLY_AUTH_TOKEN=ваш_токен_Bitly`<br>
6. Запустите скрипт<br>
   Возможные команды для запуска(из консоли, из папки с ботом):<br>
   `python3 main.py ваша_ссылка`<br>
   `python main.py ваша_ссылка`<br>
   `python3.6 main.py ссылка`<br>
   <br>
   Примеры: <br>
   `python main.py https://ya.ru`<br>
   `python main.py https://bit.ly/3qcwUP5`<br>
   
   **Примечание:** <br>
   Если вы хотите сократить ссылку, то полная ссылка должна содержать протокл `http://` или `https://`<br>