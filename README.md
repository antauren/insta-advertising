# Инструмент для конкурсов в Instagram

Cкрипт выдает список юзеров, которые:
* подписаны на автора поста  
* лайкнули пост 
* оставили комментарий, в котором упомянули своих друзей

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как авторизоваться
 
Создайте в корневой папке файл ```.env``` и пропишите в нем свои данные следующим образом:  
 ```
 USERNAME=rogozin_na_lune
 PASSWORD=s5ndl3b4IhateyouElonMaskf9eb4k6bdh
 ``` 
     
### Как запустить
```
python giveaway.py https://www.instagram.com/p/B0VXxnkAek8/
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).