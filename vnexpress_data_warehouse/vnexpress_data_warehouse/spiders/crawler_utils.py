import requests
from bs4 import BeautifulSoup


def get_article_links(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []

    load_items_div = soup.find('div', {'id': 'loadItems'})

    if load_items_div:
        for a_tag in load_items_div.find_all('a', href=True):
            link = a_tag['href']
            if 'https://vnexpress.net' in link:
                links.append(link)

    top_story_article = soup.find('article', {'class': 'item-news article-topstory'})

    if top_story_article:
        for a_tag in top_story_article.find_all('a', href=True):
            link = a_tag['href']
            if 'https://vnexpress.net' in link:
                links.append(link)

    links = list(set(links))

    return links


def is_next_page_disabled(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    next_page_button = soup.find('a', {'class': 'btn-page next-page disable'})
    return next_page_button is not None


def crawl_articles(base_url, max_pages=100):
    page_number = 1
    all_links = []

    while page_number <= max_pages:
        print(f"Crawling page {page_number}...")

        if page_number == 1:
            page_url = base_url
        else:
            page_url = f"{base_url}-p{page_number}"

        article_links = get_article_links(page_url)
        all_links.extend(article_links)
        print(article_links)

        if is_next_page_disabled(page_url):
            print("Next page button is disabled, stopping crawl.")
            break

        page_number += 1

    return all_links

