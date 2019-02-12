from selenium import webdriver
from time import sleep
from config import *


def genPageSourcesFromWeb():
	configPages = range(Config.start, Config.end)
	pageSoups = {}
	with getSeleniumDriver() as driver:
		for pageNum in configPages:
			url = getScholasticUrl(pageNum)
			logging.debug("Fetching Page %s then sleeping...", pageNum)
			driver.get(url)
			sleep(Config.pagePauseTime)  # waits for page to load
			yield driver.page_source


def getScholasticUrl(pageNum: int):
	url = "https://www.artandwriting.org/explore/online-galleries/#subset="
	url += str(pageNum)
	url += "&writing=Personal+Essay%2FMemoir&art_portfolio=false&"
	url += "writing_portfolio=false&year=0&state=All&awards=All&grade=12"
	return url


def getSeleniumDriver():
	print("Starting Selenium...", end='')
	baseProfile = webdriver.FirefoxProfile()
	# no addons
	baseProfile.set_preference("extensions.enabledScopes", 0)
	baseProfile.set_preference("extensions.autoDisableScopes", 15)

	if Config.hiddenBrowser:
		logging.warning("Hidden Browser Not implemented yet, sorry")
		# baseProfile.add_command_line_options('-headless')
		# However, on current versions of Firefox (up to and including
		# Nightly 58.0a1) running on Windows 10 this flag doesn’t seem
		# to work. Luckily, we can achieve the same effect by setting the
		# MOZ_HEADLESS environment variable either from the command line
		# with set MOZ_HEADLESS=1 or from the python script itself as above.

	driver = webdriver.Firefox(baseProfile)
	# give a bit of extra time to start up
	sleep(Config.pagePauseTime / 2)
	print("done!")
	return driver
