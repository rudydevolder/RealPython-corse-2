# ex3.11c.py Download stock quotes in CSV


import requests
import time

i = 0

# obtain quote once per minute for the next 2 minutes
while (i < 2):

    base_url = 'http://download.finance.yahoo.com/d/quotes.csv'

    # retrieve data from web server
    data = requests.get(base_url,
            params={'s': 'GOOG', 'f': 'sl1d1t1c1ohgv', 'e': '.csv'})

    # write the data to csv
    with open("stocks.csv", "a") as code:
       code.write(data.content)
    print "CSV Download Complete"
    i+=1

    # pause for 60 seconds
    time.sleep(60)
