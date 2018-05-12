# coding:utf-8

from bs4 import BeautifulSoup
import time
import re
__PRINT_INFO__ = False
SchoolName = re.compile(r'.*>(.*)<.*')
Ul = re.compile(r'(.*<li.*><span.*>).*(</span>.*<span.*>).*(</span>)')
# Ul = re.compile(r'^.*\".*?title.*?\".*>(.*)</span>\n<.*\"content.*\">(.*)<.*')


def decodeUl(ul):
    # ul = ul.strip('\n')
    match = Ul.match(ul)
    if match:
        # print(match.groups())
        # print(match.group(1))
        # print(match.group(2))
        # print(match.group(3))
        ul = ul.replace(match.group(1), '')
        ul = ul.replace(match.group(2), '#')
        ul = ul.replace(match.group(3), '')
        ul = ul.replace(' ', '')
    # print(ul.split('#'))
        ul = ul.strip()
        ul = ul.replace('；', ';')
        ul = ul.replace('：','-')
        ul = ul.replace(':','-')

        ul = ul.split('#')
        if ';' in ul[1]:
            ul[1] = ul[1].strip().split(';')
    return ul


def decodeSchoolName(sn):
    match = SchoolName.match(sn)
    if match:
        print(match.group())


def decodeFile(fileHandle):
    with open(fileHandle, encoding='gbk') as f:
        html = f.read()
        try:
            html = html.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
        except UnicodeError:
            pass
        start = time.clock()
        soup = BeautifulSoup(html, 'lxml')
        schoolInfo = []
        schoolName = soup.find_all(attrs={'id': 'School_name'})[0].string
        schoolEnName = soup.find_all(
            attrs={'id': 'School_EnglishName'})[0].string
        schoolProperties = soup.find_all(
            attrs={'id': 'School_properties'})[0].string
        schoolState = soup.find_all(attrs={'id': 'OperationState'})[0].string
        uls = soup.find_all(attrs={'class': 'list clearfix'})
        # print(soup.find_all(attrs={'id': 'School_name'}))
        # print(soup.find_all(attrs={'class': 'list clearfix'}))

        schoolInfo.append(['学校名称', schoolName.strip()])
        schoolInfo.append(['学校英文名称', schoolEnName.strip()])
        schoolInfo.append(['学校性质', schoolProperties.strip()])
        schoolInfo.append(['学校运营状态', schoolState.strip()])
        uls_text = ''
        for i in uls:
            uls_text += str(i).encode('utf-8').decode('utf-8')
        ulsli = uls_text.split('</li>')

        for i in ulsli[:-1]:
            schoolInfo.append(decodeUl(i.replace('\n', '')))

        # print(repr(ulsli[0].replace('\n', '')))
        # print(repr(ulsli[1]))
        # decodeUl(ulsli[0].replace('\n', ''))

        # uls = soup.find_all(attrs={'class': 'list clearfix'})
        # print(type(uls[0]), uls[0])
        # decodeUl(uls[0])
        if __PRINT_INFO__:
            print(len(ulsli))
            print(schoolInfo)
            print('-' * 35)
            print('Time consumed: ', time.clock() - start)

        return schoolInfo

# print(html)


if __name__ == '__main__':
    __PRINT_INFO__ = True
    decodeFile('test.html')
