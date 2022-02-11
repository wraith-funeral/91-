import re
from main import url_open


def download(title, url):
    m3u8_data = url_open(url).decode('utf8')

    # 正则表达式替换
    m3u8_data = re.sub('#E.*', '', m3u8_data).split()
    url = re.sub('index.*', '', url)

    # 拼接链接,并下载片段

    for index in m3u8_data:
        m3u8 = url + index
        content = url_open(m3u8)
        with open(f'{title}.mp4', 'ab') as fp:
            fp.write(content)
        print(f"已下载{m3u8}")

