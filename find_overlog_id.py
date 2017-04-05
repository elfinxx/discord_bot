from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://overlog.gg/")



search_form = driver.find_element_by_css_selector("#playerSearchInput")
search_form.send_keys("바트#31102")

find_button = driver.find_element_by_css_selector("#IndexContent > form > button")
find_button.submit()

current_url = driver.current_url
overlog_id = current_url.split("overview/")[1]
print(overlog_id)
driver.close()



