from bs4 import BeautifulSoup
import os
import time
import signal
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import user_email, user_paswd, data


def tox_pred(user_email, user_paswd, data):
    # global driver
    url_login = 'http://mmi-03.my-pharm.ac.jp/tox1/users/sign_in'
    # setup
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver=driver, timeout=10800)
    try:
        driver.get(url_login)
        # get login form
        form_email, form_paswd = driver.find_element_by_id("user_email"), driver.find_element_by_id("user_password")
        form_email.send_keys(user_email)
        form_paswd.send_keys(user_paswd)
        btm_login = driver.find_elements_by_name('commit')[0]
        # login
        btm_login.click()
        wait.until(EC.presence_of_all_elements_located)
        # csv upload
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[2]/a').click()
        wait.until(EC.presence_of_all_elements_located)
        form_sdf = driver.find_element_by_name('sdf')
        form_sdf.send_keys(data)
        wait.until(EC.presence_of_all_elements_located)
        # predict
        btm_predict = driver.find_element_by_xpath('//*[@id="sdf_button"]')
        time.sleep(1)
        btm_predict.click()
        # getr html
        wait.until(EC.presence_of_all_elements_located)
        for _ in range(10800):
            time.sleep(1)    
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            tag = soup.find(id="download-sdf-button")
            if tag['class'][-1] ==  'mx-2':
                time.sleep(1)
                driver.find_element_by_id('download-sdf-button').click()
                break
    finally:
        os.kill(driver.service.process.pid,signal.SIGTERM)
    

if __name__ == '__main__':
    tox_pred(user_email, user_paswd, data)