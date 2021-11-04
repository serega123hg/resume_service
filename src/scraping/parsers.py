import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ('hhru', 'rabotaru', 'vkrabota', 'work', "rabota", 'djinni')

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    ]

def hhru(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://hh.ru'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'vacancy-serp'})
            if main_div:
                div_lst = main_div.find_all('div', attrs={'class': 'vacancy-serp-item'})
                for div in div_lst:
                    title = div.find('span', attrs={'class': 'resume-search-item__name'})
                    href = title.a['href']
                    content = div.find_all('div', attrs={'class': 'vacancy-serp-item__info'})[2].text
                    company = div.find('div', attrs={'class': 'vacancy-serp-item__meta-info-company'}).text
                    logo = div.find('img')
                    if logo:
                        company = logo['alt']
                    jobs.append({'title': title.text, 'url': href,
                                 'description': content, 'company': company,
                                 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


def rabotaru(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://www.rabota.ru'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'index-page__body'})
            if main_div:
                div_lst = main_div.find_all('div', attrs={'class': 'vacancy-preview-card__wrapper white-box'})
                for div in div_lst:
                    title = div.find('h3').text.strip()
                    href = div.find('h3').a['href']
                    content = div.find_all('div', attrs={'class': 'vacancy-preview-card__content'})[0].text
                    company = div.find('div', attrs={'class': 'vacancy-preview-card__company'}).text
                    logo = div.find('img')
                    if logo:
                        company = logo['alt']
                    jobs.append({'title': title, 'url': domain + href,
                                 'description': content, 'company': company,
                                 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


def vkrabota(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://vkrabota.ru'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find_all('div', attrs={'data-test-id': 'JobCard'})
            if main_div:
               # div_lst = main_div.find_all('div', attrs={'class': 'vacancy-preview-card__wrapper white-box'})
                for div in main_div:
                    title = div.find('a').text
                    href = div.a['href']
                    content = div.find('div', attrs={'class': 'jobCard_description__19MZ1'}).text
                    company = div.find_all('span')[0].text
                    logo = div.find('img')
                    if logo:
                        company = logo['alt']
                    jobs.append({'title': title, 'url': domain + href,
                                 'description': content, 'company': company,
                                 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


def work(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:
                div_lst = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_lst:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    company = 'No name'
                    logo = div.find('img')
                    if logo:
                        company = logo['alt']
                    jobs.append({'title': title.text, 'url': domain + href,
                                 'description': content, 'company': company,
                                 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


def rabota(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://rabota.ua'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            new_jobs = soup.find('div',
                                 attrs={'class': 'f-vacancylist-newnotfound'})
            if not new_jobs:
                table = soup.find('table',
                                  id='ctl00_content_vacancyList_gridList')
                if table:
                    tr_lst = table.find_all('tr', attrs={'id': True})
                    for tr in tr_lst:
                        div = tr.find('div',  attrs={'class': 'card-body'})
                        if div:
                            title = div.find('h2',
                                             attrs={'class': 'card-title'})
                            href = title.a['href']
                            content = div.p.text
                            company = 'No name'
                            p = div.find('h2', attrs={'class': 'company-name'})
                            if p:
                                company = p.a.text
                            jobs.append({
                                'title': title.text,
                                 'url': domain + href,
                                 'description': content,
                                 'company': company,
                                 'city_id': city, 'language_id': language})
                else:
                    errors.append({'url': url, 'title': "Table does not exists"})
            else:
                errors.append({'url': url, 'title': "Page is empty"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors




def djinni(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://djinni.co'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_ul = soup.find('ul',  attrs={'class': 'list-jobs'})
            if main_ul:
                li_lst = main_ul.find_all('li',
                                          attrs={'class': 'list-jobs__item'})
                for li in li_lst:
                    title = li.find('div',
                                    attrs={'class': 'list-jobs__title'})
                    href = title.a['href']
                    cont = li.find('div',
                                   attrs={'class': 'list-jobs__description'})
                    content = cont.text
                    company = 'No name'
                    comp = li.find('div',
                                   attrs={'class': 'list-jobs__details__info'})
                    if comp:
                        company = comp.text
                    jobs.append({'title': title.text, 'url': domain + href,
                                 'description': content, 'company': company,
                                 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


if __name__ == '__main__':
    url = 'https://djinni.co/jobs/?location=%D0%9A%D0%B8%D0%B5%D0%B2&primary_keyword=Python'
    jobs, errors = djinni(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
