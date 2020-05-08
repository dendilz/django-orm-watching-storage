# Пульт охраны

Приложение для пропускного пункта, в базе данных 
которого фиксируются все посещения.

### Как установить
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей.

В linux:
```
pip install -r requirements.txt
```
В Windows:
```
python -m pip install -r requirements.txt  
```
### Как запустить
В Linux:
```
python3 main.py
```
В Windows:
```
python main.py
```
В консоли дожны увидеть
```
Performing system checks...

System check identified no issues (0 silenced).
May 08, 2020 - 11:37:56
Django version 1.11.29, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```
Далее открываем браузер и переходим на страницу http://localhost:8000/