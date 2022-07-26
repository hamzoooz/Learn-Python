from selenium import webdriver
# from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.microsoft import  EdgeChromiumDriverManager

# browser = webdriver.Chrome( ChromeDriverManager().install() )
browser = webdriver.Edge(( EdgeChromiumDriverManager().install() ))

browser.implicitly_wait(5)
browser.get("https://elzero.org")

browser.implicitly_wait(5)
browser.find_element_by_css_selector(".search-field").send_keys("Fronf-End Developer")

browser.implicitly_wait(5)



