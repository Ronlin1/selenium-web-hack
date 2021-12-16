from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.youtube.com/watch?v=eZyr8afY4bk"
no_of_views = 50
duration = float(10)

# Path where chromedriver installed : Note the slashes used:
path = "C:/ProgramData/chocolatey/lib/chromedriver/tools/chromedriver.exe"


for i in range(0,no_of_views):
    browser = webdriver.Chrome(path)
    browser.get(url)
    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)

    time.sleep(duration)

    print(str(i+1) + " iterations done")
    browser.quit()
