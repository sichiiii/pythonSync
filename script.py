
from selenium import webdriver
from PIL import Image
import time

driver = webdriver.Chrome()
driver.get('https://t.me/s/durov')


driver.set_window_size(10000, 10000)



for i in range(1, 100):
    try:
        ele = driver.find_element_by_xpath(f'/html/body/main/div/section/div[{i}]' + '/div[1]/div[2]')
    except:
        i = i-1
        ele = driver.find_element_by_xpath(f'/html/body/main/div/section/div[{i}]' + '/div[1]/div[2]')
        break
ele.screenshot('image.png')

#eleWidth = ele.size['width']
#eleHeight = ele.size['height']
#
#screenshot = driver.save_screenshot('screenshot.png')
#time.sleep(2)
#im = Image.open("screenshot.png")
#box = (ele.location['x'], ele.location['y'], ele.location['x']+eleWidth, ele.location['y']+eleHeight)
#im.crop(box).save('screenshot1.png')
#
#print(box)
#point = ele.location
