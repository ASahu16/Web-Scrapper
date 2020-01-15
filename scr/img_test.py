import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
basewidth = 300
img = Image.open('D:\img_phone.jpg')
print(img.size)
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
# img.save('sompic.jpg')
text = pytesseract.image_to_string(img, lang='eng')
print(img.size)
print(text)
