# 🤖 Data Analyst Copilot

Автоматизированный инструмент для анализа CSV-файлов и оценки качества данных.

Проект помогает Data Analyst быстро проводить первичный анализ данных (EDA), выявлять проблемы качества данных, строить визуализации и получать автоматические рекомендации с помощью AI.

---

# 🚀 Возможности

## 📊 Анализ качества данных

- количество строк и колонок
- пропущенные значения
- полные дубликаты
- дубликаты без учета ID
- расчет Data Quality Score


## 🔍 Exploratory Data Analysis (EDA)

- статистический анализ
- профиль колонок
- поиск выбросов методом IQR
- анализ числовых признаков
- корреляционный анализ
- построение графиков


## 🤖 AI-анализ

Используется локальная LLM через Ollama:

- автоматическая интерпретация результатов
- описание проблем в данных
- генерация рекомендаций


## 📄 Отчеты

- HTML отчет
- история анализов
- просмотр результатов через Streamlit


---

# 📂 Структура проекта

```text
data-analyst-copilot/

├── app/
│   ├── dashboard.py
│   ├── analyzer.py
│   ├── ai_analyzer.py
│   ├── data_loader.py
│   ├── insights.py
│   ├── quality_score.py
│   ├── report_history.py
│   └── html_report.py
│
├── reports/
│
├── images/
│   ├── main.png
│   ├── quality.png
│   ├── ai.png
│   ├── charts.png
│   └── history.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Установка и запуск

## Клонирование проекта

```bash
git clone https://github.com/SaryMustafa/data-analyst-copilot.git
```

## Создание виртуального окружения

```bash
python3 -m venv .venv
```

## Активация окружения

```bash
source .venv/bin/activate
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск приложения

```bash
streamlit run app/dashboard.py
```

---

# 📸 Интерфейс

## Главная страница

![Main](images/main.png)


## Проверка качества данных

![Quality](images/quality.png)


## AI-анализ

![AI](images/ai.png)


## Автоматические графики

![Charts](images/charts.png)


## История анализов

![History](images/history.png)


---

# 🛠 Использованные технологии

- Python 3.11
- Pandas
- Streamlit
- Matplotlib
- Seaborn
- Ollama (Llama)
- JSON
- HTML Reports


---

# 🎯 Цель проекта

Создание инструмента для автоматизации первичного анализа данных.

Проект демонстрирует навыки:

- Data Quality Analysis
- Exploratory Data Analysis
- автоматизация аналитических процессов
- визуализация данных
- применение LLM в аналитике
- разработка аналитических инструментов
