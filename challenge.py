from navigation import Browser, PageObjects
from file_manipulation import le_dados_challenge
import time


def challenge(arquivo):
    site_challenge = "https://rpachallenge.com"
    driver = Browser.chrome_browser(site_challenge)

    PageObjects.inicia_challenge(driver)

    for i in range(10):
        row = le_dados_challenge(arquivo, i)
        PageObjects.executa_challenge(driver, row)

    time.sleep(5)
