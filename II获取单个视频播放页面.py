from lxml import etree


def video_list(url_main_content):
    # 获取单个视频播放页面的链接
    tree = etree.HTML(url_main_content)
    div = tree.xpath("//a[@class='display d-block']/@href")

    # 删去前面4个杂项
    del div[0:4]

    videos = []

    # 拼接单个视频链接
    for video in div:
        url = "https://91porny.com" + video
        videos.append(url)

    return videos


print(video_list())
