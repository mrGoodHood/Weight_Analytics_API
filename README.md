WeightAnalyticsAPI — это API-сервис, позволяющий сравнивать две пользовательские аудитории по заданным SQL-условиям и вычислять процент их пересечения на основе среднего веса респондентов.

---



---

## Как запустить проект

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourname/AudienceAnalyticsAPI.git
cd AudienceAnalyticsAPI
```

### 2. Поместите файл `data.csv` в папку `data/`.

Формат данных:
```
Date,Respondent,Sex,Age,Weight
20230101,1,1,25,2.5
...
```

### 3. Запустите проект:

```bash
docker-compose up --build
```

API будет доступен по адресу: [http://localhost](http://localhost)

---

## Использование API

### GET `/getPercent`

**Описание:** Возвращает процент вхождения аудитории 2 в аудиторию 1 по среднему весу респондентов.

**Параметры:**
- `audience1`: SQL-условие для первой аудитории
- `audience2`: SQL-условие для второй аудитории

**Пример запроса:**
```
GET /getPercent?audience1=Age%20BETWEEN%2018%20AND%2035&audience2=Sex%20=%202%20AND%20Age%20>=%2018
```

**Пример ответа:**
```json
{
  "percent": 0.83333
}
```

---

## ⚙ Используемые технологии

- **Python 3.11**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Docker + docker-compose**

