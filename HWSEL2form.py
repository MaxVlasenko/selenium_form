from selenium import webdriver


login1 = "tomsmith"
login2 = "tomsmith1"
password = "SuperSecretPassword!"


def tusk1():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_css_selector('#username').send_keys(login1)
    driver.find_element_by_css_selector('#password').send_keys(password)
    driver.find_element_by_css_selector('#login > button').click()
    assert 'You logged into a secure area!' in driver.page_source
    driver.quit()


def tusk2():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_css_selector('#username').send_keys(login2)
    driver.find_element_by_css_selector('#password').send_keys(password)
    driver.find_element_by_css_selector('#login > button').click()
    assert 'Your username is invalid!' in driver.page_source
    driver.quit()


def tusk3():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_css_selector('#username').send_keys(login1)
    driver.find_element_by_css_selector('#password').send_keys(password)
    driver.find_element_by_css_selector('#login > button').click()
    assert 'You logged into a secure area!' in driver.page_source
    driver.find_element_by_css_selector('#content > div > a > i').click()
    assert 'logged out' in driver.page_source
    driver.quit()


tusk1()
tusk2()
tusk3()
