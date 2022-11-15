# 日本周辺カラー png 取得サンプル
# 保存先 : ./dst/
# https://www.jma.go.jp/bosai/weather_map/
# > python ./src/sample/sample_weathermap.py

import os
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

import urllib.error
import urllib.request

# download img from internet and save
def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            with open(dst_path, 'wb') as local_file:
                local_file.write(web_file.read())
    except urllib.error.URLError as e:
        print(e)

if __name__ == '__main__':
    # initialize
    service = Service(executable_path=EdgeChromiumDriverManager().install())
    EdgeOptions = webdriver.EdgeOptions()
    EdgeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.ChromiumEdge(service=service,options=EdgeOptions)

    # open web page
    driver.get("https://www.jma.go.jp/bosai/weather_map/")
    time.sleep(3)

    # get img
    td_class = driver.find_element(By.CLASS_NAME, 'weather-map-viewarea')
    img = td_class.find_element(By.TAG_NAME, "img")
    src = img.get_attribute('src')

    # make dir
    path_dir = "./dst/"
    os.makedirs(path_dir, exist_ok=True)

    # img get and save
    path_file = os.path.join(path_dir, os.path.basename(src))
    download_file(src, path_file)

    # debug
    print("save : ", path_file)

    # finalize
    driver.close()
