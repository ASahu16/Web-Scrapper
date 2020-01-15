
from selenium import webdriver
import urllib.request

driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver")
driver.get('https://dubai.dubizzle.com/motors/used-cars/jeep/wrangler/2019/10/5/aed1257month-2016-jeep-wrangler-sport-36l--2/?back=L21vdG9ycy9zZWFyY2gvP2tleXdvcmRzPSZpc19zZWFyY2g9MSZpc19iYXNpY19zZWFyY2hfd2lkZ2V0PTE%3D&pos=1')
img_link = driver.find_elements_by_id('phone-lead')
img_link[0].click()
number_link = driver.find_element_by_class_name('phone-num-img')
print(number_link.get_attribute('src'))
urllib.request.urlretrieve(number_link.get_attribute('src'),'D://img_phone.jpg')
driver.close()
