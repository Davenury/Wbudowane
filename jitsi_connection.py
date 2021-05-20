from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random
import string
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1,
                                                 "profile.default_content_setting_values.media_stream_camera": 1,
                                                 "profile.default_content_setting_values.geolocation": 1,
                                                 "profile.default_content_setting_values.notifications": 1
                                                 })
chrome_options.add_argument("--use-fake-ui-for-media-stream=1")
chrome_options.add_argument("--use-fake-device-for-media-stream=1")



def generate_string(length=20):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def generate_link():
    return f"https://meet.jit.si/{generate_string()}"


def click_buttons(driver: webdriver.Chrome):
    micro = driver.find_element_by_class_name("video-preview")
    camera = driver.find_element_by_class_name("video-preview")
    button = camera.find_element_by_class_name("settings-button-container")

    action_chain = ActionChains(driver)
    print(button.size)
    action = action_chain.move_to_element_with_offset(button, button.size["width"], 0)
    action.click().perform()

    sleep(2)

    first_video = driver.find_element_by_class_name("video-preview-overlay")
    action_chain = ActionChains(driver)
    action_chain.move_to_element(first_video).click().perform()

    # action_chain = ActionChains(driver)
    # action_chain.move_to_element(camera).click().perform()

    action_chain = ActionChains(driver)
    action_chain.move_to_element(micro).click().perform()


def get_driver():
    # return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)


def open_page(page_link: str, driver: webdriver.Chrome):
    driver.get(page_link)

    inputElement = driver.find_element_by_class_name("field")
    inputElement.send_keys("Intercom")

    inputElement.send_keys(Keys.ENTER)

    sleep(5)
    click_buttons(driver)

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
    open_page("https://meet.jit.si/abcd1234abcd", get_driver())
