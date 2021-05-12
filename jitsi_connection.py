from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random
import string
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1,
                                                 "profile.default_content_setting_values.media_stream_camera": 1,
                                                 "profile.default_content_setting_values.geolocation": 1,
                                                 "profile.default_content_setting_values.notifications": 1
                                                 })

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
def generate_string(length=20):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def generate_link():
    return f"https://meet.jit.si/{generate_string()}"

def click_button(driver:webdriver.Chrome):
    inputElement = driver.find_element_by_class_name("audio-preview")
    inputElement = inputElement.find_element_by_class_name("toolbox-icon")
    print(inputElement)
    inputElement.click()
    inputElement = driver.find_element_by_class_name("video-preview")
    inputElement = inputElement.find_element_by_class_name("toolbox-icon")
    print(inputElement)
    inputElement.click()



def open_page(page_link: str = "http://google.co.uk"):
    # driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
    driver.get(page_link)
    inputElement = driver.find_element_by_class_name("field")
    inputElement.send_keys("Intercom")
    inputElement.send_keys(Keys.ENTER)


    session_end = None

    while session_end is None:
        sleep(300)
        try:
            session_end = driver.find_element_by_class_name("invite-more-container")
            print(session_end)
        except NoSuchElementException:
            session_end = None

    driver.close()


if __name__ == "__main__":
    open_page("https://meet.jit.si/abcd")
