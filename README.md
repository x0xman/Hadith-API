
# Bot Hadith-API on Telegram 

> The Bot provide Hadith API and fetch content via api.hadith.sutanlab.id


## Built With

- Python
- Asynchronous
- HTTP protocol client
- Telegram-Bot

## API-Documenation
- hadith
    ```http
    GET api.hadith.sutanlab.id/books/{name}?range={number}-{number}
    ```

    **[Example]** `https://api.hadith.sutanlab.id/books/muslim?range=1-150`

    | Parameter | Type | Description |
    | :--- | :--- | :--- |
    | `number` | `0-300` | `Returns hadiths by range of number. (Note: For performance reasons, max accepted range: 300)` |
    | `name` | `['muslim','bukhari','tirmidzi','nasai','abu-daud','ibnu-majah','ahmad','darimi','malik']` | `Returns hadiths by range of number. (Note: For performance reasons, max accepted range: 300)` |
 
- spesific
    ```http
    GET api.hadith.sutanlab.id/books/{name}/{number}
    ```

    **[Example]** `https://api.hadith.sutanlab.id/books/bukhari/52`

    | Parameter | Type | Description |
    | :--- | :--- | :--- |
    | `number` | `0-300` | `Returns hadiths by range of number. (Note: For performance reasons, max accepted range: 300)` |
    | `name` | `['muslim','bukhari','tirmidzi','nasai','abu-daud','ibnu-majah','ahmad','darimi','malik']` | `Returns spesific hadith` |

- endpoints
    ```http
    GET api.hadith.sutanlab.id/books
    ```

    **[Example]** `https://api.hadith.sutanlab.id/books`

    | pattern | Type | Description |
    | :--- | :--- | :--- |
    | `https://api.hadith.sutanlab.id/books` | `list` | `Returns the list of available Hadith Books.` |
    
## Authors

👤 **Author**

- GitHub: [@x0xman](https://github.com/x0xman)
- Telegram : [@xMan](https://t.me/x0x3b)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!
