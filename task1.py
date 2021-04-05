import csv
from bot_setup import Bot, BusinessofApps

EXPORT_FILE = 'task1.csv'

if __name__ == '__main__':
    bot = Bot()
    bot_appdata = BusinessofApps(bot.driver, '/data/app-data/')
    bot_appdata.find_xpath('titles')
    names, years = bot_appdata.split_name_year()

    with open(EXPORT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(zip(names, years))

    bot.quit()