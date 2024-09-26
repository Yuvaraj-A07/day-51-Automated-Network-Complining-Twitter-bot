import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import manager as mg

PROMISED_DOWN = 14
PROMISED_UP = 6
TWITTER_EMAIL = mg.TWITTER_EMAIL
TWITTER_PASSWORD = mg.TWITTER_PASSWORD
USER_NAME = mg.USER_NAME

class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(30)
        go = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '1]/a/span[4]')
        go.click()
        time.sleep(40)
        download = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                            '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                            '1]/div/div[2]/span')
        self.down = download.text

        time.sleep(8)

        upload = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                          '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                          '2]/span')
        self.up = upload.text
        print(f"down = {self.down}")
        print(f"up = {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(20)
        mail = self.driver.find_element(By.NAME, value='text')
        mail.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(5)
        user = self.driver.find_element(By.NAME, value='text')
        user.send_keys(USER_NAME, Keys.ENTER)
        time.sleep(3)

        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(30)

        write = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span/span')
        write.send_keys(f"Hey internet provider why is my internet speed is {self.down}down/{self.up}up when I pay for "
                        f"20down/10up")
        time.sleep(2)
        post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                        '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                        '1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        post.click()


Ibot = InternetSpeedTwitterBot()

# Ibot.get_internet_speed()

Ibot.tweet_at_provider()
