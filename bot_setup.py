from selenium import webdriver
import chromedriver_autoinstaller
import re


class Bot:
    def __init__(self):
        self.path = chromedriver_autoinstaller.install()
        self.url = None
        self.driver = webdriver.Chrome(self.path)

    def start(self):
        self.driver.get(self.url)

    def stop(self):
        self.driver.quit()


class BusinessofApps(Bot):
    def __init__(self, driver, path=''):
        super().__init__()

        self.url = 'https://www.businessofapps.com' + path
        self.driver = driver
        self.xpaths = {
            'titles': '//span[@class="text__title"]',
        }
        self.titles = None
        self.start()

    def find_xpath(self, xpaths_key):
        xpath = self.xpaths[xpaths_key]
        self.titles = self.driver.find_elements_by_xpath(xpath)

    def split_name_year(self):
        years = []
        names = []
        for title in self.titles:
            element = title.get_attribute("textContent")
            name = re.sub(r'\([^)]*\)', '', element).strip()
            year = element[element.find("(")+1:element.find(")")]
            years.append(year)
            names.append(name)
        return names, years
