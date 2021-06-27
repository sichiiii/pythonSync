from flask import app
from flask.helpers import url_for
from selenium import webdriver
from sql import SQL

import app_logger

class Parser():
    def __init__(self):
        self.logger = app_logger.get_logger(__name__)
        self.sql = SQL()
        self.url = 'https://t.me/s/durov'
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--headless')
        self.option.add_argument('--disable-dev-sh-usage')
        self.option.add_argument('--disable-gpu')
        self.option.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=self.option)

    def parsePost(self):
        while 1:
            try:
                self.driver.get(self.url)

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
                url_for_image = self.url.replace('s/', '')
                link = link.replace(url_for_image+'/', '')
                print(link)
                if doesExist == 0:
                    ele.screenshot('/home/jabka/python/telegramSync/screens/' + link + '.png')
                    self.sql.addLink(link)
                return {'status':'ok'}
            except Exception as ex:
                self.logger.error(str(ex))
                return {'status':'error'}
