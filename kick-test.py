from selenium import webdriver #le driver qui te permet d'aller sur un explorateur internet
from selenium.webdriver.common.keys import Keys #ce qui te permet de rentrer des touches du clavier
import getpass #le module de mot de passe


driver = webdriver.Firefox() #ouvre Firefox
driver.get("https://www.kickstarter.com/discover/advanced?category_id=16") #ouvre vente-privee

button_load_more = driver.find_element_by_xpath('//*[@id="projects"]/div[2]/div[2]/a')
button_load_more.click()

while True:
	try:
#		time.sleep(5)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	except:
		break

