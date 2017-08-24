#dc_inside_wannaone Crawler by page num
#designed by Soo Min, JEONG

from time import strftime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

def crawl(driver, output):
    wait  = WebDriverWait(driver, 5)
    postNum = 1
    titles = driver.find_elements_by_class_name("t_subject")
    while(True):
        try:
            category= titles[postNum].find_element_by_tag_name('a').get_attribute('class')
            postNum+=1
            if (category != "icon_notice"):
                oneLink = titles[postNum].find_element_by_tag_name('a').get_attribute('href')
                print("oneLink:", oneLink)
                driver.get(oneLink)

                #collecting the contents
                contentAll = driver.find_element_by_id('dgn_content_de')
                content = contentAll.find_element_by_class_name('s_write').find_element_by_tag_name('table').text
                titleInContent = contentAll.find_element_by_class_name('wt_subject')
                edited_content = titleInContent + content('\n', ' ')
                content.replace('- dc official App', '')

                if (len(content)>3):
                    print(edited_content[4:])
                    output.write(edited_content[4:]+'\n')

                # going back to the list of titles
                driver.execute_script("window.history.go(-1)")
            else:
                print("This is a notice")
            titles = driver.find_elements_by_class_name("t_subject")

        except IndexError:
            continue

        except TimeoutError:
            driver.implicitly_wait(15)
            continue

        except OSError:
            driver.implicitly_wait(15)
            continue

    driver.quit()
    output.close()


def access(site, startPoint):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    driver.get(site)

    fileName = "WannaOne" + str(startPoint) + strftime("_%m%d_%Hh%M") + '.txt'
    print(fileName)
    output = open(fileName, "w", -1, "utf-8")

    crawl(driver, output)


def main(startPoint)
    pageNum = startPoint

    for pageNum in range(startPoint, startPoint + 1000):
        try:
            print("page:", pageNum)
            site = "http://gall.dcinside.com/board/lists/?id=wannaone&page="+str(pageNum)
            access(site, startPoint)
            pageNum+=1

        except TimeoutError:
          driver.implicitly_wait(15)
