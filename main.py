from selenium import webdriver

if __name__ == "__main__":
    chromedriver = r".\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.implicitly_wait(2)
    driver.get("https://quote.rbc.ru")
    dollar = driver.find_element_by_xpath("//a[@href='https://cash.rbc.ru/?currency=3']")
    print("Текущий курс покупки и продажи наличного доллара" + "\n" + dollar.text)
    driver.close()
