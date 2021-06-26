from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://t.me/s/dvachannel')

driver.set_window_size(10000, 10000)

for i in range(1, 100):
    try:
        ele = driver.find_element_by_xpath(f'/html/body/main/div/section/div[{i}]' + '/div[1]/div[2]')
    except:
        i = i-1
        ele = driver.find_element_by_xpath(f'/html/body/main/div/section/div[{i}]' + '/div[1]/div[2]')
        break

ele.screenshot('image.png')
