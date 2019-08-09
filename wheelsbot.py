from selenium import webdriver

driver = webdriver.Chrome("\\CODD.sis.virtual.uniandes.edu.co\Estudiantes\Profiles\lm.gomezl\Desktop\WheelsBot\lib\chromedriver.exe")
driver.set_page_load_timeout("10")
driver.get("http://google.com")
