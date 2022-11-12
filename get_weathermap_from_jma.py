from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
service = Service(executable_path=EdgeChromiumDriverManager().install())
from selenium import webdriver
EdgeOptions = webdriver.EdgeOptions()
EdgeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.ChromiumEdge(service=service)
driver.get("https://www.jma.go.jp/bosai/weather_map/")
driver.fullscreen_window()
driver.save_screenshot()

