# 1)seleniumで気象庁の実況天気図のページを開く 2)アジア太平洋域白黒の天気図を拾ってくる　3)スクリーンショットフォルダに格納する

# 時間管理用の time をインポートする
import time

# selenium関連の準備
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
service = Service(executable_path=EdgeChromiumDriverManager().install())
from selenium import webdriver
EdgeOptions = webdriver.EdgeOptions()
EdgeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.ChromiumEdge(service=service,options=EdgeOptions)

# 指定URLを開く
driver.get("https://www.jma.go.jp/bosai/weather_map/")
time.sleep(5)

# 全画面化
driver.fullscreen_window()
time.sleep(5)

# save_screenshotでdriver画面のスクショを"./*.png"で保存
driver.save_screenshot("./saved_screenshots_Folder/weathermap_now.png")


#以下、アジア太平洋域白黒の天気図の取得方法を検討中。
# WM_time = driver.find_element_by_xpath("//*[@id=\"weather-map-table\"]/div/table/tr[4]/td/div[1]")
# Picture = driver.find_element_by_xpath("//[@id=\"weather-map-table\"]/div/table/tr[5]/td/img")

# Picture_name = "JMA_weather-map" + WM_time + ".png"

# from PIL import Image
# import PIL 
# Picture = Picture.save(Picture_name)

# Picture.show
# time.sleep(10)

# 飛行場気象解説情報(定時/臨時)のページでスクリーンショット取得(デフォルトがRJTTだから操作は特に不要か)
driver.get("https://www.data.jma.go.jp/airinfo/data/awfo_comment.html#contents_area2")
time.sleep(5)
driver.save_screenshot("./saved_screenshots_Folder/RJTT_AERODOME_WX_COMMENTARY.png")