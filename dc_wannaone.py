#dc_inside_wannaone Crawler
#designed by Soo Min, JEONG

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

def crawl(driver, output):
    wait  = WebDriverWait(driver, 5)
    postNum = 1
    titles = driver.find_elements_by_class_name("t_subject")
    try:
        while(True):
            category= titles[postNum].find_element_by_tag_name('a').get_attribute('class')
            postNum+=1
            if (category != "icon_notice"):
                oneLink = titles[postNum].find_element_by_tag_name('a').get_attribute('href')
                print("oneLink:", oneLink)
                driver.get(oneLink)

                #collecting the contents
                content = driver.find_element_by_class_name('s_write').find_element_by_tag_name('table')
                edited_content = content.text.replace('\n', ' ')
                print("content:", edited_content)
                output.write(edited_content)

                #collecting replies
                replypages = driver.find_element_by_class_name('gallery_re_paging')
                replypages = replypages.find_elements_by_tag_name('a')
                for oneReplyPage in replypages[1:]:
                    replies = driver.find_elements_by_class_name('reply')
                    for oneReply in replies:
                        reply_content = oneReply.text
                        if (len(reply.text) > 3):
                            print(reply_content)
                            output.write(reply_content)
                    oneReplyPage.click()

                # going back to the list of titles
                driver.execute_script("window.history.go(-1)")
            else:
                print("This is a notice")
            titles = driver.find_elements_by_class_name("t_subject")

    except IndexError:
        print("last post")

    except TimeoutError:
        driver.implicitly_wait(15)

    driver.quit()
    output.close()


def access(site):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    driver.get(site)

    fileName = "WannaOne" + strftime("_%m%d_%Hh%M") + '.txt'
    print(fileName)
    output = open(fileName, "w", -1, "utf-8")

    crawl(driver.output)

def main():
    pageNum = 1

    try:
        while(True):
            print("page:", pageNum)
            site = "http://gall.dcinside.com/board/lists/?id=wannaone&page="+str(pageNum)+"&exception_mode=recommend"
            access(site)
            pageNum+=1

    except Exception:
        print ("end of the board")

main()