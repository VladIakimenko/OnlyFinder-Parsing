import time
import sys
import undetected_chromedriver
from selenium.webdriver.common.keys import Keys


class UnDetChrome:
    def __init__(self):
        self.driver = undetected_chromedriver.Chrome()
        self.driver.start_client()

    def parse(self, url, timer):
        self.driver.get(url)

        time_start = int(time.time())
        while True:
            self.driver.find_element('tag name', 'body').send_keys(Keys.END)
            sys.stdout.write('\r' + f' {round(((int(time.time()) - time_start) * 100) / timer)}%')
            sys.stdout.flush()
            if int(time.time()) - time_start >= timer:
                with open('data/start_from.lnk', 'wt') as f:
                    f.write(self.driver.current_url)
                break

        html = self.driver.page_source

        with open('data/parsed_page.html', 'w', encoding="utf-8") as f:
            f.write(html)

        return html

    def terminate(self):
        self.driver.close()
