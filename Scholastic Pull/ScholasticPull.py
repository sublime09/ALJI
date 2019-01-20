from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup


def printDict(d, level=0):
    indent = '\t'*level
    for k, v in d.items():
        if isinstance(v, dict):
            print(indent, k, ":{")
            printDict(v, level=level+1)
            print(indent, "}")
        else:
            print(indent, k, ":", v)


def getSeleniumDriver():
    print("Starting Selenium...", end='')
    baseProfile = webdriver.FirefoxProfile()
    baseProfile.set_preference("extensions.enabledScopes", 0)  # no addons
    baseProfile.set_preference("extensions.autoDisableScopes", 15)  # no addons
    driver = webdriver.Firefox(baseProfile)
    print("done!")
    return driver


def iterUrls():
    urlBegin = "https://www.artandwriting.org/explore/online-galleries/#subset="
    urlEnd = "&writing=Personal+Essay%2FMemoir&art_portfolio=false&writing_portfolio=false&year=0&state=All&awards=All&grade=12"
    totalSubsets = int(543 / 15) + 1
    for subsetNum in range(1, totalSubsets + 1):
        fullUrl = urlBegin + str(subsetNum) + urlEnd
        yield fullUrl


def driverUrlToSoup(driver, url):
    print("getting page ...", end='')
    driver.get(url)
    sleep(3)  # waits for page to load
    print(" souping ...", end='')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print(" done!")
    return soup


def main():
    entries = []
    with getSeleniumDriver() as driver:
        for url in iterUrls():
            soup = driverUrlToSoup(driver, url)
            for entry in soup.select('div.writing-content'):
                entries.append(entry)

            break  # do only one page/url for now

    for e in entries[-4:]:
        story = contentToStory(e)
        print(story)
        print("\n\n\n")


def contentToStory(content):
    tags = content.select('h1,h2,h3,h4,h5,p')

    def iterToLines(tags):
        emptySpace = 0
        for t in tags:
            line = t.text.strip()
            if line == '':
                emptySpace += 1
                if emptySpace == 2:
                    yield ''
            else:
                yield line
                emptySpace = 0
    lines = iterToLines(tags)
    story = '\n\t'.join(lines)
    return story


if __name__ == '__main__':
    main()
