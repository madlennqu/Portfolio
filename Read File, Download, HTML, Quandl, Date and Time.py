#Read/Write file example code
# Read file

file = open("/Users/madlennqu/PycharmProjects/pythonprog/econ3086/AAPL.csv", "r")
# read one line
file.readline()
# Go back to the beginning
file.seek(0)
# Loop
for line in file:
    print(line)

# close file
file.close()

# if you don't want to close the file by yourself
with open("/Users/madlennqu/PycharmProjects/pythonprog/econ3086/AAPL.csv","r") as file:
    for line in file:
        print(line, end="")
        
# Write (Overwrite)
out_file = open("/Users/madlennqu/PycharmProjects/pythonprog/econ3086/example456.csv",'w') 
out_file.write("I'm Susan\n")
out_file.close()
# Write (Append)   
out_file = open("/Users/madlennqu/PycharmProjects/pythonprog/econ3086/example456.csv",'a') 
out_file.write("I'm Susan\n")
out_file.close()
# Write without need to close file
with open("/Users/madlennqu/PycharmProjects/pythonprog/econ3086/example456.csv",'a') as out_file:
    for i in range(10):
        out_file.write("{},{},{}\n".format(i,i**2,i**i))

#Read write file exercise
#downloaded csv file from Yahoo finance: https://finance.yahoo.com/quote/AAPL/history?p=AAPL
# read the file and print the date and close price
# wrote the data to another file with a new column, "Day changes" which is close / open -1
with open("AAPL.csv", "r") as in_file:
    with open("AAPL_out.csv", "w") as out_file:
        header = in_file.readline()
        out_file.write("Date,Close,Day Changes\n")
        for line in in_file:
            line = line.strip()
            (date, open_p, high, low, close, adj_c, vol) = line.split(",")
            changes = float(close) / float(open_p) - 1
            out_file.write("{},{},{}\n".format(date, close, changes))

#Get HTML file content
import urllib.request as ur
api_key = "xxx_xxx_xxx_xxx_xxx"
response = ur.urlopen("https://www.quandl.com/api/v3/datatables/WIKI/PRICES?ticker=AAPL&api_key="+api_key)
print(response.read().decode())

#Download File
import urllib.request as ur
url = "https://cdn.sstatic.net/Sites/stackoverflow/img/apple-touch-icon.png"
ur.urlretrieve(url,"stackoverflow.png")

#Get data from Quandl (with API)
import quandl
quandl.ApiConfig.api_key = 'xxxxxxxxxxxx'
df = quandl.get('BITFINEX/BTCEUR')
Get Data from coinmarketcap (with request)
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
def get_latest_price(symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': symbol
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'your-key-here',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data["data"][symbol]["quote"]["USD"]["price"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

#Date & Time
import datetime as dt
# Current time
dt.datetime.now()
# Print time
dt.datetime.now().strftime("%Y-%m-%d %H:%M")
# create date
mydate = dt.date(1943,3, 13)  #year, month, day
mydatetime = dt.datetime(2003,6,28,12,4,5)
# add/minus numbernof days
tomorrow = dt.datetime.now() + dt.timedelta(days=1)
# diff between dates
mydatetime - dt.datetime.now()
