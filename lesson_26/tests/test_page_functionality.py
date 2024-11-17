from pytest import mark
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


@mark.parametrize('frame_path, input_path, secret_text, button_path', [
    ("//iframe[@id='frame1']", "//input[@id='input1']", "Frame1_Secret", "//input[@id='input1']/../button"),
    ("//iframe[@id='frame2']", "//input[@id='input2']", "Frame2_Secret", "//input[@id='input2']/../button")
])
def test_page_functionality(driver, frame_path, input_path, secret_text, button_path):
    frame_el = driver.find_element(By.XPATH, frame_path)
    driver.switch_to.frame(frame_el)

    input_el = driver.find_element(By.XPATH, input_path)
    input_el.send_keys(secret_text)

    button_el = driver.find_element(By.XPATH, button_path)
    button_el.click()

    alert = Alert(driver)

    assert_that(alert.text).is_equal_to("Верифікація пройшла успішно!")

    alert.accept()
