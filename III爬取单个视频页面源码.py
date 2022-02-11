from bs4 import BeautifulSoup

from main import url_open


def get_m3u8(video_page_url):
    # 解析
    content = url_open(video_page_url).decode('utf8')
    soup = BeautifulSoup(content, 'lxml')
    title = soup.select('title')[0]
    title = title.get_text()
    # 获取m3u8的地址
    tag = soup.select('video[data-src]')[0]

    m3u8_url = tag.attrs.get('data-src')  # 获取data-src的值

    return [title, m3u8_url]
