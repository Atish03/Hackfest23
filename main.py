from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import getOTP

EMAIL_ID = "b3gul4.infosec@gmail.com"
FILTERS = {
	"popularity": "/html/body/div[3]/div/div[2]/section[2]/article/section[2]/div/section/section[1]",
	"rating":     "/html/body/div[3]/div/div[2]/section[2]/article/section[2]/div/section/section[2]",
	"time":       "/html/body/div[3]/div/div[2]/section[2]/article/section[2]/div/section/section[3]",
	"cost":       "/html/body/div[3]/div/div[2]/section[2]/article/section[2]/div/section/section[4]"
}

def getElement(xpath, parent = "default", max_tries = 20):
	done = False

	while not done:
		try:
			driver.switch_to.default_content()
			if parent != "default":
				driver.switch_to.frame(driver.find_element(By.XPATH, parent))
				time.sleep(1)
			done = True
		except Exception as e:
			time.sleep(1)
			print(e)
			pass

	element = None
	tries = 0
	while element == None and tries != max_tries:
		try:
			element = driver.find_element(By.XPATH, xpath)
		except Exception as e:
			tries += 1
			time.sleep(1)
			print(e)
			pass

	return element

def launchBrowser(location):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("start-maximized")
	chrome_options.add_argument("load-extension=./Extension")
	driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options)

	driver.get(f"https://www.zomato.com/{location}")
	return driver

def login(driver):
	try:
		getElement("/html/body/div[1]/div/div[2]/header/nav/ul[2]/li[2]").click()
		getElement("/html/body/div[2]/div/div[2]/section[2]/section/div[3]", parent = "/html/body/div[7]/iframe").click()
		getElement("/html/body/div[2]/div/div[2]/section[2]/section/section/section/input", parent = "/html/body/div[7]/iframe").send_keys(EMAIL_ID)
		getElement("/html/body/div[2]/div/div[2]/section[2]/section/button", parent = "/html/body/div[7]/iframe").click()

		time.sleep(5)

		OTP = getOTP.OTP()

		for i in range(1, 7):
			getElement(f"/html/body/div[2]/div/div[2]/section[2]/section/div/div/div/input[{i}]", parent = "/html/body/div[7]/iframe").send_keys(OTP[i - 1])
	except:
		print("Unable to login, please try again!")

def sortby(filter):
	driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/div/div[1]").click()
	getElement(FILTERS[filter]).click()
	driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/section[2]/section/div/button[2]").click()

def getDetails(categoryType, element):
	data = {}

	if categoryType == "best_food":
		data["title"] = element.find_element(By.XPATH, ".//div/a[2]/div[1]/h4").text
		data["rating"] = element.find_element(By.XPATH, ".//div/a[2]/div[1]/div/div/div/div/div/div[1]").text
		data["price"] = element.find_element(By.XPATH, ".//div/a[2]/div[2]/p[2]").text
		data["order_url"] = element.find_element(By.XPATH, ".//div/a[1]").get_attribute("href")

	return data

def order(order_url):
	driver.get(order_url)
	all_foods = getElement("/html/body/div[1]/div/main/div/section[4]/section/section[1]").find_elements(By.XPATH, ".//*")
	food_items = list(map(lambda x: x.text, all_foods))
	print(food_items)

driver = launchBrowser("mirzapur")
# login(driver)

while True:
	try:
		inp = input(">>> ")
		data = getDetails("best_food", driver.find_elements(By.CLASS_NAME, "active-selected")[0])
		if inp == "s":
			filter = input("sortby: ")
			sortby(filter)
			time.sleep(2)
			driver.refresh()
		elif inp == "o":
			print(data)
			order(data["order_url"])
	except Exception as e:
		print(e)
		pass 