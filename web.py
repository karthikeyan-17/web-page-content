import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    """Get the html from the web page
    :parameter url of the webpage
    :return the html content"""

    html=requests.get(url)
    return html.content


def parse_html_using_tag(html_content,tag):
    """To convert  html format to text file content
     :parameter the html content tag for paragraph
     :return text file data"""
    soup = BeautifulSoup(html_content, 'html.parser')
    data = [para.text for para in soup.find_all(tag)]
    return (data)




