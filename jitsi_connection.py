from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random
import string
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import sys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1,
                                                 "profile.default_content_setting_values.media_stream_camera": 1,
                                                 "profile.default_content_setting_values.geolocation": 1,
                                                 "profile.default_content_setting_values.notifications": 1,
                                                 "hardware.audio_capture_enabled":True,
                                                 "hardware.video_capture_enabled":True
                                                 })
chrome_options.add_argument("--use-fake-ui-for-media-stream=1")


def generate_string(length=20):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def generate_link():
    return f"https://meet.jit.si/{generate_string()}"


def click_buttons(driver: webdriver.Chrome):
    camera = driver.find_element_by_class_name("video-preview")
    button = camera.find_element_by_class_name("settings-button-container")

    action_chain = ActionChains(driver)
    action = action_chain.move_to_element_with_offset(button, button.size["width"], 0)
    action.click().perform()

    sleep(2)

    first_video = driver.find_element_by_class_name("video-preview-overlay")
    action_chain = ActionChains(driver)
    action_chain.move_to_element(first_video).click().perform()

    # action_chain = ActionChains(driver)
    # action_chain.move_to_element(camera).click().perform()

    micro = driver.find_element_by_class_name("audio-preview")
    button = micro.find_element_by_class_name("settings-button-container")
    action_chain = ActionChains(driver)
    action = action_chain.move_to_element_with_offset(button, button.size["width"], 0)
    action.click().perform()
    sleep(2)
    how_many_elements = micro.find_element_by_class_name("audio-preview-content")
    print(how_many_elements.get_attribute("innerHTML"))
    #
    # first_audio = driver.find_elements_by_class_name("audio-preview-microphone")
    # print(f"How many: {len(first_audio)}")
    # action_chain = ActionChains(driver)
    # action_chain.move_to_element(first_audio).click().perform()

    action_chain = ActionChains(driver)
    action_chain.move_to_element(micro).click().perform()


def get_driver():
    # return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)


def open_page(page_link: str, driver: webdriver.Chrome = get_driver()):
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
    url = "https://meet.jit.si/abcd1234abcd" if len(sys.argv) == 1 else sys.argv[1]
    print(f"url:{url}")
    open_page(url, get_driver())
