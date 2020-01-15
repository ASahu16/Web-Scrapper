import requests as r
import urllib.request
import bs4
import pytesseract
from PIL import Image
from io import BytesIO
import base64


data=r.request('get','https://dubai.dubizzle.com/motors/auto-accessories-parts/car4x4-parts/batteries/2019/10/7/genuine-land-rover-battery-for-all-models--2-2/?back=L21vdG9ycy9zZWFyY2gvP2tleXdvcmRzPSZpc19zZWFyY2g9MSZpc19iYXNpY19zZWFyY2hfd2lkZ2V0PTE=&shownumber')
s=bs4.BeautifulSoup(data.text,'html.parser')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
basewidth = 300
j = s.findAll('div', class_='phone-content')
i = j[1].findAll('img')
print(type(i[0]))


img_data = i[0].get('src')
print(img_data)
urllib.request.urlretrieve(i[0].get('src'),'imgPhn.jpg')
img = Image.open('imgPhn.jpg')
# here next three line of code are used to increasae the size of image
# tesseract cannot read the image beacuse it is very small in size
# so vey increade the size of image
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
# img.save('sompic.jpg')

text = pytesseract.image_to_string(img, lang='eng')
print(text)



# test program 1
# with open("imageToSave.png", "wb") as fh:
#     fh.write(base64.decodebytes(img_data))
#
# fd = urllib.urlopen(i[0].get('src'))
# image_file = io.BytesIO(fd.read())




# test program 2
# urllib.request.urlretrieve(i[0].get('src'))
#
#
#
# response_img = r.get(i[0].get('src'))
# # img = Image.open(BytesIO(response_img.content))
# # img = Image.open(urllib.request.urlretrieve(i[0].get('src')))
# buffered = BytesIO(response_img.content)
# image.save(buffered, format="JPEG")
# img = base64.b64encode(buffered.getvalue())
#
#
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), Image.ANTIALIAS)
# # img.save('sompic.jpg')
# text = pytesseract.image_to_string(img, lang='eng')
# print(text)
