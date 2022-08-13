import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()
options.headless=True
options.add_argument('--headless')
driver = uc.Chrome(options=options)
driver.get(f'https://instagram.com/lksjdgjdsg')

if 'Sorry, this page isn\'t available.' in driver.page_source:
    print("hi")
else:
    print("bye")