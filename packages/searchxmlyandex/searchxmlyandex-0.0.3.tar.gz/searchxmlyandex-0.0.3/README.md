Yandex XML Search

You can easily convert XML data to JSON data which fetched from YandexXMLSearch API.

Prerequisites:
+ requests

Usage
Example usage shown as below.

from searchxmlyandex.YandexXMLSearch import YandexXMLSearch
user, api_key = 'username','api_key'
query = raw_input('Search Term: ')
parser = YandexXMLSearch(user,api_key,query)

Method List:
- getQuery
- setQuery
- search
- getTotalPageCount
- getTotalResultCount
- getAllResults
- getResponseDate
- getJSONObject
- getResultJSONString

Authors:
Ataberk Yavuzer - https://github.com/0xSaiyajin
