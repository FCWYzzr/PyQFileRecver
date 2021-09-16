import pickle as pkl
from sys import argv

result = "请将程序生成的.map文件拖到本程序图标上以打开"
if len(argv) > 0:
    if len(argv) > 1:
        result = "本程序仅能打开单个文件，请逐个打开"
    else:
        with open(argv[1],"rb") as f:

