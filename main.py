import requests 
import datetime as DT

today = DT.date.today()
yesterday = today - DT.timedelta(days=1)
link = 'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=' + str(yesterday) +'&to=' + str(today) + '&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c'

r = requests.get(link)


content =r.json()
articles = content["articles"]

for article in articles:
  print(article["title"], article["description"])

def get_news(topic, start_day, end_day, language = 'en', api_key = '890603a55bfa47048e4490069ebee18c'):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}stock%20market&from{start_day}&to={end_day}&sortBy=popularity&={language}&apiKey={api_key}'
  r = requests.get(url)
  results = []
  content = r.json()
  for article in articles:
    results.appednd(article["title"], article["description"])
