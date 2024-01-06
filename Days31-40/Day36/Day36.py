## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
# If you do not want to send a text, send a email. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests
import os
import datetime

# ---------- CONTSANTS ---------- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# ---------- FUNCTIONS ---------- #
def isFivePercent(day1: float, day2: float):
  percentageDifference = ((day2 - day1) / day1) * 100
  if percentageDifference > 5:
    return f"⬆️ {round(percentageDifference, 2)}"
  elif percentageDifference < -5:
    return f"⬇️ {round(percentageDifference, 2)}"
  else:
    return False

# ---------- DATE VARIABLES ---------- #
yesterdayDate = datetime.datetime.now() - datetime.timedelta(days=1)
dayBeforeYesterdayDate = datetime.datetime.now() - datetime.timedelta(days=2)
formattedYesterdayDate = yesterdayDate.strftime("%Y-%m-%d")
formattedDayBeforeYesterdayDate = dayBeforeYesterdayDate.strftime("%Y-%m-%d")

# ---------- APLHA VANTAGE VARIABLES ---------- #
avResponse = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={AV_API_KEY}")
avResponse.raise_for_status()
avData = avResponse.json()

yesterdaysClosingPrice = float(avData["Time Series (Daily)"][formattedYesterdayDate]["1. open"])
dayBeforeYesterdayClosingPrice = float(avData["Time Series (Daily)"][formattedDayBeforeYesterdayDate]["1. open"])

if isFivePercent(dayBeforeYesterdayClosingPrice, yesterdaysClosingPrice) != False:
  newsResponse = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={formattedYesterdayDate}&to={formattedDayBeforeYesterdayDate}&language=en&sortBy=popularity&apiKey={NEWS_API_KEY}")
  newsResponse.raise_for_status()
  newsData = newsResponse.json()
  articleNumber = 0
  for _ in range(3):
    article = f"Percent Difference: {isFivePercent(dayBeforeYesterdayClosingPrice, yesterdaysClosingPrice)}\nTitle: {newsData['articles'][articleNumber]['title']}\nDescription: {newsData['articles'][articleNumber]['description']}"
    print(article)
    articleNumber += 1