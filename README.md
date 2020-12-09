<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="test_budget_back_0"></a>test_budget_back</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">Развертывание проекта.</p>
<pre><code>Скачать проект:
</code></pre>
<p class="has-line-data" data-line-start="6" data-line-end="7">git clone <a href="https://github.com/Srg300/test_budget_back">https://github.com/Srg300/test_budget_back</a></p>
<pre><code>После скачивания:
</code></pre>
<p class="has-line-data" data-line-start="9" data-line-end="14">Создаем папку test_budget_back и в консоли пишем команды:<br>
cd test_budget_back<br>
python3 -m venv budget_venv<br>
source budget_venv/bin/activate<br>
pip3 install -r requirements.txt</p>
<p class="has-line-data" data-line-start="15" data-line-end="17">делаем миграции:<br>
python3 <a href="http://manage.py">manage.py</a> migrate</p>
<p class="has-line-data" data-line-start="18" data-line-end="19">создаем супер пользователя</p>
<p class="has-line-data" data-line-start="20" data-line-end="21">Далее импортирование данных в БД доступна из админки Django</p>
<p class="has-line-data" data-line-start="22" data-line-end="26">В приложении Apitools, создается модель “Ссылки для запросов”<br>
Модель имеет 2 поля.<br>
url - для ссылки импорта данных<br>
Type budget - для выбора типа бюджета</p>
<p class="has-line-data" data-line-start="27" data-line-end="28">При сохранении модели, запускается импорт в БД по выбранному типу модели</p>
