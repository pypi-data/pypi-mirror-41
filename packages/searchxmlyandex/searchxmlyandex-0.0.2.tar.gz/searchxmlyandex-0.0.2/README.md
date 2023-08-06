# Yandex XML Search

You can easily convert XML data to JSON data which fetched from YandexXMLSearch API.

### Dependencies

* Python<=2.7

### Prerequisites

* requests

### Installing
```
pip install searchxmlyandex
```

## Usage

Example usage as shown below.

```
from searchxmlyandex.YandexXMLSearch import YandexXMLSearch

user, api_key = 'username','api_key'
query = raw_input('Search Term: ')
parser = YandexXMLSearch(user,api_key,query)

```

### Method List

* getQuery
* setQuery
* search
* getTotalPageCount
* getTotalResultCount
* getAllResults
* getResponseDate
* getJSONObject
* getResultJSONString

## Authors

* **Ataberk Yavuzer** - [0xSaiyajin](https://github.com/0xSaiyajin)

See also the list of [contributors](https://github.com/0xSaiyajin/searchxmlyandex/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
