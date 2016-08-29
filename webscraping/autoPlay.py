from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_class_name('container')

keyOptions = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT]
while True:
    try:
        htmlElem.send_keys(random.choice(keyOptions))
    except KeyboardInterrupt:
        raise Exception('Finished running the code.')