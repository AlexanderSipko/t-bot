
1. git clone https://github.com/AlexanderSipko/t-bot.git
2. cd t-bot 'переход в директорию проекта'
3. py -m venv .venv 'создание вируального окружения для библиотек'
4. .venv\Script\activate 'запуск виртуального окружения для библиотек'
5. pip install -r requirements.txt 'установка библиотек'
6. create .env file and add TOKEN=... 'создание файла с названием .env где указан логин от телеграм бота'
7. py ./telegram_bot.py 'запуск телеграм бота'



>>
пример .env файл
TOKEN=700000000:AAGAAAAAAAAAAAAAAAAAAAAAAA
>>