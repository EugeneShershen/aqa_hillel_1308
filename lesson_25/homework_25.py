from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")


def xpath_locators(web_driver: WebDriver):
    try:
        web_driver.find_element(By.XPATH, "//a[@class='header_logo']")
        web_driver.find_element(By.XPATH, "//a[@class='btn header-link -active']")
        web_driver.find_element(By.XPATH, "//nav[contains(@class,'d-flex')]/*[text()='About']")
        web_driver.find_element(By.XPATH, "//button[text()='Contacts']")
        web_driver.find_element(By.XPATH, "//div[contains(@class,'header_right')]/*[contains(text(),'log')]")
        web_driver.find_element(By.XPATH, "//button[@class='btn btn-outline-white header_signin']")
        web_driver.find_element(By.XPATH, "//section[@class='section hero']")
        web_driver.find_element(By.XPATH, "//div[@class='hero-descriptor']/h1")
        web_driver.find_element(By.XPATH, "//p[contains(text(),'the help')]")
        web_driver.find_element(By.XPATH, "//button[contains(@class,'hero-descriptor_btn')]")
        web_driver.find_element(By.XPATH, "//div[contains(@class,'about-picture')]/img[contains(@src,'1')]")
        web_driver.find_element(By.XPATH, "//p[text()='Log fuel expenses']")
        web_driver.find_element(By.XPATH, "//div[@class='about-block']/p[contains(text(),'replacement')]")
        web_driver.find_element(By.XPATH, "//div[contains(@class,'mt-sm-4')]/div/div/img")
        web_driver.find_element(By.XPATH, "//p[@class='about-block_title h2'][contains(text(),'manuals')]")
        web_driver.find_element(By.XPATH, "//*[contains(text(),'100 instructions')]")
        web_driver.find_element(By.XPATH, "//div[@id='contactsSection']")
        web_driver.find_element(By.XPATH, "//h2[text()='Contacts']")
        web_driver.find_element(By.XPATH, "//a[contains(@href,'facebook')]")
        web_driver.find_element(By.XPATH, "//div[contains(@class,'flex-column')]/a[contains(@class,'display-4')]")
        web_driver.find_element(By.XPATH, "//div[contains(@class,'flex-column')]/*[contains(text(),'support')]")
        web_driver.find_element(By.XPATH, "//footer[@class='footer d-flex align-items-center']")
        web_driver.find_element(By.XPATH, "//p[contains(text(),'©')]")
        web_driver.find_element(By.XPATH, "//p[contains(text(),'©')]/../*[last()]")
        web_driver.find_element(By.XPATH, "//a[@class='footer_logo']")

        print("All elements was found correctly!")

    except WebDriverException as e:
        print(f"Error: {e}")


def css_locators(web_driver: WebDriver):
    try:
        web_driver.find_element(By.CSS_SELECTOR, "a.header_logo")
        web_driver.find_element(By.CSS_SELECTOR, "a.btn.header-link.-active")
        web_driver.find_element(By.CSS_SELECTOR, "nav.d-flex")
        web_driver.find_element(By.CSS_SELECTOR, "nav.header_nav button:first-of-type")
        web_driver.find_element(By.CSS_SELECTOR, "div.header_right button.header-link")
        web_driver.find_element(By.CSS_SELECTOR, "div.header_right *.btn.btn-outline-white.header_signin")
        web_driver.find_element(By.CSS_SELECTOR, "section.section.hero")
        web_driver.find_element(By.CSS_SELECTOR, "*.hero-descriptor h1")
        web_driver.find_element(By.CSS_SELECTOR, "p.hero-descriptor_descr")
        web_driver.find_element(By.CSS_SELECTOR, "button.hero-descriptor_btn")
        web_driver.find_element(By.CSS_SELECTOR, "div.about-picture img[src*='1']")
        web_driver.find_element(By.CSS_SELECTOR,
                                "div[class='col-12 col-lg-6'] div.about-block p.about-block_title.h2")
        web_driver.find_element(By.CSS_SELECTOR,
                                "div[class='col-12 col-lg-6'] div.about-block p.about-block_descr.lead")
        web_driver.find_element(By.CSS_SELECTOR, "div.mt-sm-4 div div img")
        web_driver.find_element(By.CSS_SELECTOR, "div.mt-sm-4 div.about-block p.about-block_title.h2")
        web_driver.find_element(By.CSS_SELECTOR, "div.mt-sm-4 div.about-block p.about-block_descr.lead")
        web_driver.find_element(By.CSS_SELECTOR, "div#contactsSection")
        web_driver.find_element(By.CSS_SELECTOR, "div.col-md-6 h2")
        web_driver.find_element(By.CSS_SELECTOR, "a[href*='facebook']")
        web_driver.find_element(By.CSS_SELECTOR, "div.flex-column a.display-4")
        web_driver.find_element(By.CSS_SELECTOR, "div.flex-column *[href*='@ithillel.ua']")
        web_driver.find_element(By.CSS_SELECTOR, "footer.footer.d-flex.align-items-center")
        web_driver.find_element(By.CSS_SELECTOR, "div.footer_item.-left p:first-of-type")
        web_driver.find_element(By.CSS_SELECTOR, "div.footer_item.-left p:last-of-type")
        web_driver.find_element(By.CSS_SELECTOR, "a.footer_logo")

        print("All elements was found correctly!")

    except WebDriverException as e:
        print(f"Error: {e}")
