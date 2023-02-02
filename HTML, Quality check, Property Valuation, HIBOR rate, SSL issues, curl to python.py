#HTML
https://www.w3schools.com/html/default.asp

#Beach Water Quality (out dated)
import urllib.request
import bs4
url = "https://cd.epic.epd.gov.hk/EPICDI/beach/grading/"
response = urllib.request.urlopen(url)
text = response.read().decode()
html = bs4.BeautifulSoup(text, 'html.parser')

def get_beach_water_quality(beach_code):
    url = "https://cd.epic.epd.gov.hk/EPICDI/beach/gradingreport/{}/".format(beach_code)
    response = urllib.request.urlopen(url)
    text = response.read().decode()
    html = bs4.BeautifulSoup(text, 'html.parser')

    grade = html.find("div",attrs={"class" : "grade_caption"}).text.strip().split(" : ")[1]

    #print(grade)
    return grade

#get_beach_water_quality("hom")

for element in html.find_all("div",attrs={"class" : "btn_beach_fix_size"}):
    try:
        beach_name = element.find("a").text.strip()
        beach_code = element.find("a")["onclick"].split("\\'")[-2]
        print("{} - {}".format(beach_name, get_beach_water_quality(beach_code)))
    except AttributeError:
        pass


#Get Property Valuation
import requests
import json
def get_valuation(flat):
    headers = {
        'Connection': 'keep-alive',
        'X-HSBC-Chnl-CountryCode': 'HK',
        'X-HSBC-Src-UserAgent': '',
        'X-HSBC-Src-Device-Id': '',
        'X-HSBC-Channel-Id': 'PWS',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'X-HSBC-Locale': 'en_HK',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-HSBC-Chnl-Group-Member': '',
        'Origin': 'https://www.hangseng.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.hangseng.com/',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    data = '{"area":"H","district":"CB","estate":"DR","block":"13545","floor":"0004","flat":"'+flat+'","carpark":"","tcKnowledge":"on","hpContactUs":""}'

    response = requests.post('https://rbwm-api.hsbc.com.hk/pws-hk-hase-mortgage-eapi-prod-proxy/v1/evaluation/address/valuation', headers=headers, data=data)

    result = json.loads(response.text)
    return result["valuation"]

print(get_valuation("A"))


#HIBOR rate
import urllib.request
import bs4
import datetime as dt
hkab_url = "http://www.hkab.org.hk/hibor/listRates.do?lang=en&Submit=Search&year={}&month={}&day={}"

def get_one_month_hibor(year, month, day):
    try:
        response = urllib.request.urlopen(hkab_url.format(year, month, day))
        text = response.read().decode()
        html = bs4.BeautifulSoup(text, 'html.parser')

        overnight = float(html.find("td",text="Overnight").parent.find_all("td")[1].text)
        one_week = float(html.find("td",text="1 Week").parent.find_all("td")[1].text)
        two_week = float(html.find("td",text="2 Weeks").parent.find_all("td")[1].text)
        one_month = float(html.find("td", text="1 Month").parent.find_all("td")[1].text)
        two_month = float(html.find("td", text="2 Months").parent.find_all("td")[1].text)
        three_month = float(html.find("td", text="3 Months").parent.find_all("td")[1].text)
        six_month = float(html.find("td", text="6 Months").parent.find_all("td")[1].text)
        twelve_month = float(html.find("td", text="12 Months").parent.find_all("td")[1].text)

        return (overnight,one_week,two_week,one_month,two_month,three_month,six_month,twelve_month)
    except:

        return (float('NaN'),float('NaN'),float('NaN'),float('NaN'),float('NaN'),float('NaN'),float('NaN'),float('NaNprint(get_one_month_hibor(2018,2,14))
print(get_one_month_hibor(2018,2,14))

#Reference: POST Request
Click https://docs.python.org/3.7/howto/urllib2.html#data link to open resource

#Get beach grade by beach code
import urllib.request
import bs4

def get_beach_grade(beach_code):
    url = "https://cd.epic.epd.gov.hk/EPICDI/beach/gradingreport/{}/".format(beach_code)
    response = urllib.request.urlopen(url)
    text = response.read().decode()
    html = bs4.BeautifulSoup(text, 'html.parser')

    grade_div = html.find("div", attrs={"class" : "grade_caption"})
    grade = grade_div.text.strip().split(" : ")[1]
    return grade

print(get_beach_grade("oc"))
print(get_beach_grade("cp"))
print(get_beach_grade("b"))

#HIBOR (code in class)

import urllib.request
import bs4

def get_hibor(year,month,day):
    url = "https://www.hkab.org.hk/hibor/listRates.do?lang=en&Submit=Search&year={}&month={}&day={}".format(year,month,day)
    response = urllib.request.urlopen(url)
    text = response.read().decode()
    html = bs4.BeautifulSoup(text, 'html.parser')

    try:
        overnight = html.find("td", text="Overnight").parent.find_all("td")[-1].text
        one_week = html.find("td", text="1 Week").parent.find_all("td")[-1].text

    except:
        overnight = "NaN"
        one_week = "NaN"

    return overnight, one_week

import time

for day in range(1,31):
    hibors = get_hibor(2015,7,day)
    print(type(hibors))
    print(hibors[0])
    print(hibors[1])
    time.sleep(2)

#Beach Quality (code in class 13 Nov)

import urllib.request
import bs4
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
def get_beach_grade(beach_code):
    url = "https://cd.epic.epd.gov.hk/EPICDI/beach/gradingreport/{}/".format(beach_code)
    response = urllib.request.urlopen(url)
    text = response.read().decode()
    html = bs4.BeautifulSoup(text, 'html.parser')
    return html.find("div", attrs={"class": "grade_caption"}).text.strip().split(" : ")[1]
    
url = "https://cd.epic.epd.gov.hk/EPICDI/beach/grading/"
response = urllib.request.urlopen(url)
text = response.read().decode()
html = bs4.BeautifulSoup(text, 'html.parser')
beaches_elem = html.find_all("div", attrs={"class":"btn_beach_fix_size"})
for beach_ele in beaches_elem:
    try:
        code = beach_ele.find("a")["onclick"].split("'")[-4]
        name = beach_ele.find("a").text.strip()
        grade = get_beach_grade(code)

        print("{},{},{}".format(name, code, grade))
    except:
        print("error on processing {}".format(beach_ele))


#Work around for SSL issues
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#curl to python request convertor
Click https://curlconverter.com/ link to open resource.
