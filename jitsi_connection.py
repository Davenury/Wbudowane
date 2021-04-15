from selenium import webdriver
from time import sleep
import random
import string
from webdriver_manager.chrome import ChromeDriverManager
from configurationsGetter import get_id

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1,
                                                 "profile.default_content_setting_values.media_stream_camera": 1,
                                                 "profile.default_content_setting_values.geolocation": 1,
                                                 "profile.default_content_setting_values.notifications": 1
                                                 })

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


def generate_string(length=20):
    letters = string.ascii_letters
    print(''.join(random.choice(letters) for i in range(length)))


def generate_link():
    return f"https://meet.jit.si/{get_id()}/{generate_string()}"


def open_page(page_link: str = "http://google.co.uk"):
    driver.get(page_link)
    sleep(10)
    driver.close()


if __name__ == "__main__":
    open_page("https://meet.jit.si/abcd")
    sleep(10000)
