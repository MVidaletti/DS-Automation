import csv
from bot_setup import Bot, BusinessofApps

bot = Bot()
bot_appdata = BusinessofApps(bot.driver, '/data/app-data/')
bot_appdata.find_xpath('titles')
names, years = bot_appdata.split_name_year()


with open('task1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(names, years))
