from selenium import webdriver
import chromedriver_autoinstaller
import re
import time



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
            'name_n_year' : '//span[@class="text__title"]',
            'content_menu' : '//ul[@class="scroll-spy-list"]//li',
            'back_to_AppData' : '//a[@href="/data/"]'
        }
        self.titles = None
        self.start()

    def find_xpath(self, xpaths_key):
        xpath = self.xpaths[xpaths_key]
        self.web_elements = self.driver.find_elements_by_xpath(xpath)
        return self.web_elements

  
    def get_name_year_content(self):
        names, years, contents, contents_pack  = [], [], [], []
        app_data_web_elements = self.find_xpath('name_n_year')
        print(f'----------->{app_data_web_elements} <-------------')
        for web_element in app_data_web_elements:
            name_n_year = web_element.get_attribute("textContent")
            name = re.sub(r'\([^)]*\)', '', name_n_year).strip()
            year = name_n_year[name_n_year.find("(")+1:name_n_year.find(")")]
            names.append(name)
            years.append(year)
            print(f'{names} \n\n')
            print(f'{years} \n\n')

            web_element.click()
            print(f'----------->{app_data_web_elements} <-------------')
            content_web_element = self.find_xpath('content_menu')
            for content in content_web_element:
                content = content_web_element.get_attribute("textContent")
                contents_pack.append(content)
            contents.append(tuple(contents_pack))
            contents_pack = []
            go_back_web_element = self.driver.find_element_by_xpath('//a[@href="/data/"]')
            print(f'----------->{go_back_web_element} <-------------')
            go_back_web_element[0].click()
            time.sleep(1)
        return names, years, contents





