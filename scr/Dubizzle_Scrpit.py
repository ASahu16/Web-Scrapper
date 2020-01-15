import requests
import csv
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image
import urllib.request

file = open('dataFile2.csv', 'w', newline = '')
writer = csv.writer(file)

page = requests.get("https://dubai.dubizzle.com/motors/search/?keywords=&is_search=1&is_basic_search_widget=1")
# print(page.status_code) use it to check the status of page, FUTURE IMPROVEMENT
soup = BeautifulSoup(page.content, 'html.parser')
# soup.find_all('h2', id_='title')
for title_span in soup.find_all('h2', id='title'):
    # here we define the variable item_link which is used to store the lick tag inside the span
    item_link = title_span.find_all('a')
    # item_page_request is used to store the actual page for each itme from the list page
    item_page_request = requests.get(item_link[0].get('href'))
    item_page = BeautifulSoup(item_page_request.content, 'html.parser')
    # print(item_page.status_code) use it to check the status of page, FUTURE IMPROVEMENT
    item_title = item_page.find('span', id='listing-title-wrap')
    item_currency = item_page.find('span', itemprop="priceCurrency")
    item_price = item_page.find('span', id='actualprice')


    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    basewidth = 300
    j = item_page.findAll('div', class_='phone-content')
    i = j[1].findAll('img')
    urllib.request.urlretrieve(i[0].get('src'), 'imgPhn.jpg')
    img = Image.open('imgPhn.jpg')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # img.save('sompic.jpg')
    text_phn = pytesseract.image_to_string(img, lang='eng')



    item_picture = item_page.find_all('img')
    img_link = "none"
    for j in item_page.findAll('div'):
        if (j.get('id') == "photos"):
            for i in j.findAll('img'):
                img_link = i.get('src')
                break
    # here data is a variable to store a tuple in the excel sheet
    data = [item_title.text, item_currency.text+'\t'+item_price.text, text_phn, img_link]
    writer.writerow(data)

