# Банковский виджет операций

Проект для фильтрации и сортировки банковских операций по статусу и дате.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Bogdana222495/bank-operations-widget.git
2. (Опционально) Установи нужные инструменты для проверки кода
pip install flake8 mypy isort
3. Использование
В модуле src.processing есть две функции:

filter_by_state(operations, state="EXECUTED")

Фильтрует список операций — оставляет только те, у которых статус (state) совпадает с указанным.

Параметры:
operations — список словарей с операциями.
state — строка, например "EXECUTED" или "CANCELED". По умолчанию "EXECUTED".
 Возвращает: новый список с отфильтрованными операциями.
 Пример: from src.processing import filter_by_state

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
]

# Оставить только выполненные операции
executed = filter_by_state(data)
# Оставить только отменённые
canceled = filter_by_state(data, "CANCELED")
sort_by_date(operations, reverse=True)

Сортирует операции по дате.

Параметры:
operations — список словарей с операциями.
reverse — порядок сортировки:
True — по убыванию (сначала новые), по умолчанию
False — по возрастанию (сначала старые)
 Возвращает: новый отсортированный список.
 Пример:from src.processing import sort_by_date

# Сначала самые свежие операции
sorted_new_first = sort_by_date(data)

# Сначала самые старые
sorted_old_first = sort_by_date(data, reverse=False)
4. Структура проекта
bank-operations-widget/
├── src/
│   └── processing.py     # здесь находятся функции
├── README.md             # это файл — инструкция
└── .gitignore            # скрывает ненужные файлы
5. Требования
Python 3.8 или новее
Для проверки кода: flake8, mypy, isort (можно установить через pip)

6. Модуль `generators`

Новый модуль для работы с большими объёмами транзакций с использованием генераторов. Позволяет эффективно фильтровать, извлекать описания и генерировать номера карт.

7. Функции

#### `filter_by_currency(transactions, currency)`
Возвращает итератор по транзакциям с указанной валютой.

```python
usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
# {
#   "id": 939719570,
#   "state": "EXECUTED",
#   ...
#   "operationAmount": { "currency": { "code": "USD" } }
# }

   