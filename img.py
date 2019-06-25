#*****************************************************************************
# Author:Lingyin
# Date:2019-06-25
# 函数功能：下载给定地址的图片，田英章毛笔楷书
#*****************************************************************************
import urllib.request
import time
import random

base = "http://taim9.com/wp-content/uploads/img/2019022721/20190227-"


def imgs_list(base):
    imgs = []
    for i in range(17993, 18192):
        imgs.append(base + str(i) + ".jpg")
    return imgs


def download():
    imgCount = 0
    for img_url in imgs_list(base):
        img = urllib.request.urlopen(img_url)
        with open('./TYZ/' + str(imgCount) + ".jpg", "wb") as f:
            f.write(img.read())
            print("Num %d has been downloaded" % imgCount)
            imgCount += 1

        # 延时2-3秒
        time.sleep(random.randint(2, 3))


if __name__ == '__main__':
    download()
