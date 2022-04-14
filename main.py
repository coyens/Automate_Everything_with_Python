import requests 
import datetime as DT

today = DT.date.today()
yesterday = today - DT.timedelta(days=1)
link = 'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=' + str(yesterday) +'&to=' + str(today) + '&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c'

r = requests.get(link)


content =r.json()
print(link)