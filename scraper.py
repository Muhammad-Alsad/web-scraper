import requests
from  bs4 import BeautifulSoup



URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    citations_needed = []
    all_anchors = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")

    for anchor in all_anchors:
        citations_needed.append(anchor.find('span', text="citation needed").text.strip())

    return len(citations_needed)


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    all_paragraphs = []
    all_anchors = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")

    for anchor in all_anchors:
        all_paragraphs.append(anchor.parent.parent.parent.text.strip())

    report = '\n\n'.join(all_paragraphs)
    
    return report


if __name__=="__main__":
      print(get_citations_needed_report(URL))
      print(get_citations_needed_count(URL))