from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time,sys

def get_image(url, pic_name):
    chromedriver = r"chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    chrome_options = Options()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    driver.set_window_size(1920,1080)
    driver.get(url)
    time.sleep(1)
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(width,height)
    driver.set_window_size(width, height)
    time.sleep(1)
    driver.save_screenshot(pic_name)
    driver.close()

url = str(sys.argv[1])
# now = int(round(time.time()*1000))
# pic_name = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now/1000))+".png"
pic_name = 'pic.png'
get_image(url, pic_name)
exit()
