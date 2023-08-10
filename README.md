# Blog-site


# Технологии
### 1. Frontend:
* html5
* css3
* javascript

### 2. Backend:
* Django
* DRF
* Pillow

\* Полный список библиотек в файле requirements.txt

# Развертывание 

1. Сделайте Fork и клонируйте репозиторий: 
```
git clone git@github.com:suvorika/blog_site.git 
```
2. Далее начинайте работать с зависимостями. Перейдите в директорию с бэкенд-приложением проекта, создайте и активируйте виртуальное окружение, установите пакеты из файла requirements.txt:
```
# Переходим в директорию backend-приложения проекта.
cd blog_site/backend/
# Создаём виртуальное окружение.
python -m venv venv
# Активируем виртуальное окружение.
source venv/Scripts/activate
# Возвращаемся назад 
cd ..
# Устанавливаем зависимости.
pip install -r requirements.txt
```
3. Заключительный шаг перед запуском бэкенд-приложения — выполните миграции и создайте суперюзера, чтобы протестировать работу панели администратора. Для этого из директории, в которой находится файл manage.py, выполните команды:
```
# Применяем миграции.
python manage.py migrate
# Создаём суперпользователя.
python manage.py createsuperuser
```
4. Запускаем приложение с помощью команды: python manage.py runserver


### Автор: [Андрей Суворв](https://github.com/suvorika)