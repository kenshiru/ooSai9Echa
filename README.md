Все фразы и категории лежат в `categories-collection.json`.

# Перед запуском
Ставим dev зависимости
```
pip3 install -r requirements-dev.txt
```

Прогоним тесты
```
python3 -m pytest ./tests/test_*.py
```

Ставим зависимости приложения
```
pip3 install -r requirements.txt
```


Запускаем приложение
```
python3 server.py
```
Сервер слушает все интерфейсы на порту **5000** (зашито в коде)

# API
> GET /categories?phrase=some%20phrase  

Вернет список имён категорий, элементам которых соответсвует данная
параметром `phrase` фраза.

Пример:
```
curl -XGET http://localhost:5000/categories?phrase=тайская%20кухня
```
