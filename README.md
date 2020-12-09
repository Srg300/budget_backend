# test_budget_back

Развертывание проекта.

    Скачать проект:

git clone https://github.com/Srg300/test_budget_back

    После скачивания:
Создаем папку test_budget_back и в консоли пишем команды:
cd test_budget_back
python3 -m venv budget_venv
source budget_venv/bin/activate
pip3 install -r requirements.txt

делаем миграции:
python3 manage.py migrate

создаем супер пользователя

Далее импортирование данных в БД доступна из админки Django

В приложении Apitools, создается модель "Ссылки для запросов"
Модель имеет 2 поля. 
url - для ссылки импорта данных
Type budget - для выбора типа бюджета

При сохранении модели, запускается импорт в БД по выбранному типу модели



