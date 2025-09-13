import requests

stock_endpoint ="https://www.alphavantage.co/query"
News_endpoint ="https://newsapi.org/v2/top-headlines/sources"
alphavantage_key = "2KGCAC15X2T5J226"
News_api_key="3f46f020ed43484da66a4694b36db4cb"

news_parameters = {
    "apikey":News_api_key,
    "category":"business",
    "language": "en",
    "country": "us",
}

name = "Tesla Inc"

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "apikey": alphavantage_key,

}
stocks_request = requests.get(url=stock_endpoint, params= stock_parameters)
stocks_request.raise_for_status()
stocks_data = stocks_request.json()
print(stocks_data)

news_request = requests.get(url=News_endpoint, params=news_parameters)
news_request.raise_for_status()
news_data = news_request.json()
print(news_data)