# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск


- Скачайте код;
- Запустите виртуальное окружение;
- Установите зависимости:
```
pip install -r requirements.txt
```
### Для добавления продукции на сайт загрузите свой образец таблицы (можно Excel) в следующем формате:

| Категория    | Название            | Сорт            | Цена | Картинка                 | Акция                |
|--------------|---------------------|-----------------|------|--------------------------|----------------------|
| Белые вина   | Белая леди          | Дамский пальчик | 100  | Rbelaya_ledi.png         | Выгодное предложение |
| Напитки      | Коньяк классический |                 | 100  | konyak_klassicheskyi.png |                      |
| Красные вина | Черный лекарь       | Качич           | 200  | chernyi_lekar.png        |                      |

- Запустите сайт командой:
```
python main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
