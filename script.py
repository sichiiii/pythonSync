from flask import app
from selenium import webdriver
from sql import SQL

import app_logger

class Parser():
    def __init__(self):
        self.logger = app_logger.get_logger(__name__)
        self.sql = SQL()
        self.driver = webdriver.Chrome()

    def parsePost(self):
        try:
            self.driver.get('https://t.me/s/durov')

            self.driver.set_window_size(10000, 10000)

            for i in range(1, 100):
                try:
                    ele = self.driver.find_element_by_xpath(f'/html/body/main/div/section/div[{i}]' + '/div[1]/div[2]')
                except:
                    i = i-1
                    ele = self.driver.find_element_by_xpath(f'/html/body/main/div/section/div[{i}]' + '/div[1]/div[2]')
                    link_ele = self.driver.find_element_by_xpath(f'/html/body/main/div/section/div[{i}]' + '/div[1]/div[2]/div[3]/div/span[3]/a')
                    break

            link = link_ele.get_attribute('href')
            doesExist = self.sql.checkDoesExist(link)
            if doesExist == 0:
                ele.screenshot('image.png')
                self.sql.addLink(link)
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}
