from selenium import webdriver #le driver qui te permet d'aller sur un explorateur internet
from selenium.webdriver.common.keys import Keys #ce qui te permet de rentrer des touches du clavier
from re import sub
from decimal import Decimal



driver = webdriver.Firefox() #ouvre Firefox
driver.get("https://www.kickstarter.com/discover/advanced?category_id=16") #ouvre vente-privee

button_load_more = driver.find_element_by_xpath('//*[@id="projects"]/div[2]/div[2]/a')
button_load_more.click()

list_of_all_the_cards = driver.find_elements_by_css_selector(".js-react-proj-card")

list_of_all_the_interesting_projects = []

for card in list_of_all_the_cards:
	print("==========")
	div_name = card.find_element_by_css_selector(".type-16")
	link = div_name.find_element_by_css_selector('a').get_attribute("href")
	print(link)
	list_of_mr2 = card.find_elements_by_css_selector('.mr2')
	funds_raised_in_string = list_of_mr2[1].find_element_by_css_selector('.navy-600').text
	funds_raised = Decimal(sub(r'[^\d.]', '', funds_raised_in_string))
	print(funds_raised)
	percentage_in_string = list_of_mr2[2].find_element_by_css_selector('.navy-600').text
	percentage = Decimal(sub(r'[^\d.]', '', percentage_in_string))
	print(percentage)
	if funds_raised > 100000 or percentage > 100:
		print("It's a match !")
		dictionnaire = {
			"url": link,
			"amount_raised": funds_raised,
			"percentage": percentage
		}
		list_of_all_the_interesting_projects.append(dictionnaire)

print(list_of_all_the_interesting_projects)