from urllib.request import urlopen
from os.path import join, exists
from os import mkdir, getcwd


def SaveImg(url, name):
    pic = urlopen(url).read()
    dir = join(getcwd(), "/DataCollected/image")
    dirs = dir[3:].strip("/").split("/")
    dir = ""
    for d in dirs:
        dir += d + '/'
        if not exists(dir):
            mkdir(dir)

    with open(dir + name + ".png", "wb+") as f:
        f.write(pic)
