from lxml import etree
from io import StringIO
import json
import os
import parser
import config


if __name__ == '__main__':
    print(" Opening browser. Please, wait this may take a while...")
    driver = parser.UnDetChrome()
    print(" Opened.")

    while True:
        print(' Please, set the time limit for this session.'
              ' Next session will continue from where this one drops.\n'
              ' Keep on loading content for (enter time in seconds):', end='\t')

        while True:
            timer = input().strip()
            if timer.isdigit():
                timer = int(timer)
                break

        print()
        print(" Collecting data...")

        if not os.path.exists(config.DATA_PATH):
            os.mkdir(config.DATA_PATH)

        if os.path.exists(config.START_FROM):
            with open(config.START_FROM, 'rt') as f:
                link = f.read()
        else:
            link = config.BASE_URL

        html = driver.parse(link, timer=timer)

        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(html), parser)

        containers = tree.xpath('//*[@class="result-container col-sm-7"]')

        result = []

        if os.path.exists(config.PRODUCT):
            with open(config.PRODUCT, 'r', encoding='UTF-8') as filehandle:
                result = json.load(filehandle)

        counter = 0
        for cont in containers:
            name = ''.join(cont.xpath('./a/h3/text()'))
            if name in [account['name'] for account in result]:
                continue

            if name:
                counter += 1
                result.append(
                    {'name': name,
                     'link': ''.join(cont.xpath('./a/@href')),
                     'count': ''.join([c for c in
                                       str(cont.xpath('./div[@class="profile-info"]'
                                                      '/span/strong[1]/text()'))
                                       if c.isdigit()])}
                              )

        if result:
            with open(config.PRODUCT, 'w', encoding='UTF-8') as filehandle:
                json.dump(result, ensure_ascii=False, indent=4, fp=filehandle)

        print()
        print(f' {counter} items added to result.json. {len(result)} records total.')

        print()
        cmd = input(' Keep on? (any key to continue)\n "q" or "e" for "quit"\t').casefold().strip()
        if cmd in ('q', 'exit', 'quit', 'esc', 'e', 'end'):
            driver.terminate()
            break

