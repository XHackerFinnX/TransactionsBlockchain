# Задание 1
## Источники
Нашел информацию из [Ссылка на источник](https://bitcoin.stackexchange.com/questions/40893/how-to-access-latest-transactions-using-the-blockchain-info-api)

Использовал этот **сайт для API** [Ссылка на api](https://www.blockchain.com/ru/explorer/api/blockchain_api). От туда взял Unconfirmed Transactions: https://blockchain.info/unconfirmed-transactions?format=json с лимитом 100

## Структура проекта
**main.py**: Основной скрипт, который запускает процесс сбора транзакций и записи в базу данных.

**transactions.py**: Модуль для получения данных о транзакциях с API блокчейна.

**database.py**: Модуль для работы с базой данных SQLite.

**tx.py**: Модуль для работы. Предоставляет метод для вставки данных и получение данных о транзакциях в базе данных.

**tx_csv.py** Скрипт, который запускает процесс записи данных о транзакциях в CSV-файл.

## Описание проекта

Скрипт, который по API из сети Bitcoin раз в 10 минут берет 100 последних уникальных транзакций из блокчейна и считает объём исходящих и входящих транзакций для кошельков, участвующих в этих транзакциях. Должна быть поднята база, в которую записываются хэши транзакций, кошельки, участвующие в транзакциях, объемы транзакций по кошелькам. Результатом выполнения задания является выгрузка из базы за 6 часов работы скрипта и исходный код скрипта.

## Проверка проекта и шаги установки

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/XHackerFinnX/TransactionsBlockchain.git
   cd TransactionsBlockchain
   ```
      1.1 **Просмотр базы данной**
        Данные о транзакциях в базе данной SQLite по пути `base/bitcoin_transaction.db`.
        В таблице `transactions` хранятся следующие данные:

         hash: Хэш транзакции.

         type_wallet: Входящий или исходящий адрес кошелька.

         wallet: Адрес кошелька.

         volume: Объем транзакции.

         datetime: Время записи транзакции.

2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate   # Для Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Запустите файл:**
   ```bash
   cd src
   python main.py
   ```

## Фотографии работы проекта
Логи проекта
![Логи проекта](https://github.com/XHackerFinnX/TransactionsBlockchain/blob/main/photo_readme/log.png)
![Логи проекта конец](https://github.com/XHackerFinnX/TransactionsBlockchain/blob/main/photo_readme/log_end.png)

Данные в БД
![Данные](https://github.com/XHackerFinnX/TransactionsBlockchain/blob/main/photo_readme/data.png)
