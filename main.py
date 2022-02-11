import urllib.parse
import urllib.request
from II获取单个视频播放页面 import video_list
from III爬取单个视频页面源码 import get_m3u8
from IV下载单个m3u8视频 import download


def url_open(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62"
    }

    #  (1)请求对象的定制
    request = urllib.request.Request(url=url, headers=headers)  # 定制请求对象

    # 返回爬取结果
    response = urllib.request.urlopen(request)

    # 阅读内容并转码
    content = response.read()

    return content


def main(url_main):
    url_main_content = url_open(url_main).decode('utf8')  # 获取视频列表页面源码

    videos = video_list(url_main_content)  # 获取该页面所以视频主页链接

    for video_page_url in videos:
        data = get_m3u8(video_page_url)  # 获取页面title和m3u8链接
        title = data[0]
        url = data[1]

        download(title, url)  # 下载单个视频
        print('ok')


if __name__ == '__main__':
    # 爬取的视频菜单主页
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page, end_page + 1):
        url_main = 'https://91porny.com/author/%E6%A0%A1%E6%9C%8D%E7%BB%88%E7%BB%93%E8%80%85&page=' + str(page)
        main(url_main)
