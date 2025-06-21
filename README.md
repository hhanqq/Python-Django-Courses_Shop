Учебный проект один из первых в моей истории.

Этот проект представляет собой **веб-приложение на Django** с админкой, моделью курсов и категорий, а также REST API через библиотеку **Tastypie**.

---

# 🛒 Django Course Shop

Веб-приложение для отображения и управления курсами.  
Позволяет:
- Просматривать список курсов по категориям.
- Просматривать детали каждого курса.
- Управлять данными через Django Admin.
- Получать данные через REST API.

---

## 🧰 Стек технологий

| Категория       | Используемые технологии |
|----------------|-------------------------|
| **Фреймворк**   | Django 5.x              |
| **База данных** | SQLite (по умолчанию) / PostgreSQL/MySQL (опционально) |
| **API**         | Tastypie               |
| **Шаблоны**     | Django Templates + Bootstrap |
| **Админка**     | Django Admin            |
| **Миграции**    | Django Migrations       |

---

## 📋 Описание

Проект состоит из двух основных частей:

### 1. **Frontend (шаблоны Django)**  
- Главная страница: вывод всех курсов (`/`)
- Страница курса: детальная информация о курсе (`/course/<id>`)
- Базовые шаблоны HTML с использованием Bootstrap

### 2. **Backend**
- Модели:
  - `Category`: категории курсов
  - `Course`: сам курс с полями: название, цена, количество студентов, отзывы и т.п.
- Админ-панель:
  - Возможность добавлять/редактировать курсы и категории
  - Inline редактирование курсов в категории
- REST API:
  - Доступ к данным через `/api/v1/courses` и `/api/v1/categories`
  - Защита API через кастомную аутентификацию
- Поддержка миграций Django

---

## 🧠 Архитектура

### 1. **Модели**

#### `Category`
```python
class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
```

#### `Course`
```python
class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
```

### 2. **Django Admin**
- Поддерживает:
  - Редактирование категорий и курсов
  - Встроенный интерфейс для добавления курсов внутри категории
  - Настройка отображения полей
  - Группировка и фильтры

Пример:
```python
class CoursesInline(admin.TabularInline):
    model = models.Course
    extra = 1
```

### 3. **REST API (Tastypie)**
- Реализованы два ресурса:
  - `CategoryResource`
  - `CourseResource`
- Поддержка метода GET
- Кастомная аутентификация:
```python
class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        ...
```

### 4. **Миграции**
- Автоматически генерируются через команды Django:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧩 Структура проекта

```
django-course-shop/
├── base/
│   ├── settings.py          # Конфигурация проекта
│   ├── urls.py              # URL маршруты
│   └── wsgi.py              # WSGI настройки
├── shop/
│   ├── models.py            # Модели курсов и категорий
│   ├── views.py             # Представления
│   ├── urls.py              # URL маршруты приложения
│   ├── admin.py             # Админ-панель
│   └── migrations/          # Миграции базы данных
├── api/
│   ├── models.py            # Ресурсы Tastypie
│   ├── authentication.py    # Кастомная аутентификация
│   └── urls.py              # API маршруты
├── templates/
│   └── shop/
│       ├── courses.html     # Шаблон списка курсов
│       └── single_course.html # Шаблон страницы курса
├── manage.py                # Точка входа
└── requirements.txt         # Зависимости
```

---

## ⚙️ Установка и запуск

### 1. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 2. Примените миграции:
```bash
python manage.py migrate
```

### 3. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

### 4. Запустите сервер:
```bash
python manage.py runserver
```

---

## ✅ Возможности для доработки

- Добавить регистрацию и покупку курсов.
- Интеграция платежных систем (Stripe, Yookassa).
- Авторизация через OAuth2.
- Фильтрация и поиск курсов.
- Кэширование API через Redis.
- Тестирование с помощью `pytest` или `unittest`.
- Деплой на VPS или платформы типа Render, Railway, Heroku.

---
