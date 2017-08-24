#dc_inside_wannaone by each name Crawler
#designed by Soo Min, JEONG

#Input the "startPoint" and "endPoint", which are the numbers of the first post and the last post to be crawled.

from time import strftime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time, strftime
from multiprocessing import Pool


def main():
    startPoint = #HERE!
    endPoint = #HERE!

    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    fileName = "WannaOne" + str(startPoint)+strftime("_%m%d_%Hh%M") + '.txt'
    output = open("text/"+fileName, "a", 1, "utf-8")


    for postNum in range(startPoint,endPoint):
        try:
            site = "http://gall.dcinside.com/board/view/?id=wannaone&no="+str(postNum)
            driver.get(site)
            wait = WebDriverWait(driver, 5)

            title = driver.find_element_by_class_name("wt_subject")
            content = driver.find_element_by_class_name("s_write").find_element_by_tag_name('table')
            tAndC = title.text[4:]+' '+content.text.replace('\n',' ')
            output.write(str(postNum) + '\t' + tAndC+'\n')
            print (str(postNum) + '\t' + tAndC)

        except TimeoutException:
            driver.implicitly_wait(20)
            continue

        except TimeoutError or RuntimeError or OSError:
            driver.implicitly_wait(20)
            continue

        except NoSuchElementException:
            continue

        except NoSuchWindowException:
            continue

        except OSError:
            continue


    output.close()
    driver.quit()

main()
#
# if __name__ == '__main__':
#     start_time = time()
#     coreNum = 6
#     pool = Pool(processes=coreNum)
#     args = [3952, 33473, 51700, 83672, 104188, 133405]
#
#     pool.map(main, args)
#     print("--- %s seconds ---", (time.time()- start_time))
#
#
