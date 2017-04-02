#!/usr/bin/python3

import os
import sys
import shutil

#reload(sys)
#setdefaultencoding('gbk')
def search(path, word,destdir):
#    print(path,word)
    allfile = os.listdir(path)
#    print(allfile)
    for name in allfile:
        fp = os.path.join(path, name)
        if os.path.isfile(fp):
            with open(fp,encoding='gbk',errors="ignore") as f:
                for line in f:
                    if word in line:
                        shutil.copy(fp,destdir)
                        print(fp)
                        break
        elif os.path.isdir(fp):
            search(fp, word,destdir)

search(sys.argv[1], sys.argv[2],sys.argv[3])