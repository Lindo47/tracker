# Техническое задание: Аналитический трекер электроники для комиссионок

## 1. Цель
Сервис для учета и анализа маржинальности б/у техники.

## 2. Роли
- Гость: просмотр каталога.
- Оценщик: управление устройствами и транзакциями.

## 3. Модели
1. Condition: grade_name, description, price_modifier.
2. Device: name, brand, base_market_price, condition (ForeignKey).
3. Transaction: device (ForeignKey), transaction_type, actual_price, date.

## 4. Функционал
- Расчет цены выкупа на основе состояния.
- Учет прибыли по сделкам.
- Аналитика рентабельности через Pandas/Matplotlib.