
from selenium import webdriver
from PIL import Image
import time

driver = webdriver.Chrome()
driver.get('https://t.me/s/durov')


driver.set_window_size(10000, 10000)

ele = driver.find_element_by_xpath('/html/body/main/div/section/div[19]/div[1]')
eleWidth = ele.size['width']
eleHeight = ele.size['height']

screenshot = driver.save_screenshot('screenshot.png')
time.sleep(2)
im = Image.open("screenshot.png")
box = (ele.location['x'], ele.location['y'], ele.location['x']+eleWidth, ele.location['y']+eleHeight)
region = im.crop(box)
region.show()
region.save('screenshot1.png')

point = ele.location

print(box)