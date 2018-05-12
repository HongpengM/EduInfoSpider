from selenium import webdriver
browser = webdriver.Chrome()
from time import sleep
from bs4 import BeautifulSoup
import os.path as osp
import random
# browser.switch_to.alert.accept()
# browser.add_cookie(
#     {'name': 'Hm_lvt_b47523672ea7966981f87de0f8661ca4', 'value': 1523956436})
# browser.add_cookie(
#     {'name': 'Hm_lpvt_b47523672ea7966981f87de0f8661ca4', 'value': 1523956612})
browser.get('http://data.xinxueshuo.cn/nsi/user/login.html')


def indexGen(i):
    if len(str(i)) == 1:
        return '000' + str(i)
    elif len(str(i)) == 2:
        return '00' + str(i)
    elif len(str(i)) == 3:
        return '0' + str(i)
    else:
        return str(i)


sleep(15)
for i in range(1140):
    url = "http://data.xinxueshuo.cn/nsi/school/detail.html?School_name=10" + \
        indexGen(i + 1) + '&whereFrom=search'
    filename = indexGen(i + 1) + '.html'
    browser.get(url)
    html = BeautifulSoup(browser.page_source, 'lxml')
    html = html.prettify()
    try:
        html = html.encode('gbk', 'ignore').decode('gbk', 'ignore')
    except UnicodeError:
        pass
    with open(osp.join('C:\\Users\\K\\Desktop\\NSIdata\\html', filename), 'w') as f:
        f.write(html)
    sleep(1 + random.random() * 2)
