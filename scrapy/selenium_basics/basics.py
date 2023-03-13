from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
driver.get("https://duckduckgo.com")

search_input = driver.find_element_by_xpath('(//input[contains(@class,"js-search-input")])[1]')
search_input.send_keys("My User Agent")
search_input.send_keys(Keys.ENTER)
# search_btn = driver.find_element_by_id('search_button_homepage')
# search_btn.click()

print(driver.page_source)

driver.close()